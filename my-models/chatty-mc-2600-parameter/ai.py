import numpy as np
from pathlib import Path

np.random.seed(42)

training_data = [
    ("king", "queen"),
    ("cool", "fresh"),
    ("fire", "hot"),
    ("smart", "great"),
    ("trash", "bad"),
    ("fast", "strong"),
    ("brave", "bold"),
    ("rich", "supreme"),
    ("legend", "goat"),
    ("champion", "elite"),
    ("weak", "soft"),
    ("loser", "mid"),
    ("boring", "slow"),
    ("lame", "basic"),
    ("dumb", "silly"),
    ("fake", "mean"),
    ("rude", "mean"),
    ("lost", "sad"),
    ("happy", "loud"),
    ("quiet", "cold"),
]

vocab = [
    "cool",
    "king",
    "goat",
    "fire",
    "legend",
    "champion",
    "elite",
    "supreme",
    "smart",
    "queen",
    "brave",
    "great",
    "fast",
    "strong",
    "rich",
    "fresh",
    "clean",
    "wild",
    "bold",
    "real",
    "pure",
    "loser",
    "weak",
    "mid",
    "trash",
    "bad",
    "lame",
    "boring",
    "slow",
    "broke",
    "fake",
    "dumb",
    "soft",
    "basic",
    "silly",
    "clumsy",
    "messy",
    "lazy",
    "rude",
    "mean",
    "lost",
    "happy",
    "sad",
    "tall",
    "small",
    "old",
    "new",
    "hot",
    "cold",
    "loud",
    "quiet",
]

vocab_size = 51
embed_size = 8
num_heads = 3

INIT_SCALE = 0.01
LEARNING_RATE = 0.005
GRAD_CLIP = 1.0
WEIGHT_CLIP = 5.0
CHECKPOINT_DIR = Path(__file__).resolve().parent / "model_ckpt"
SAVE_EVERY = 100


def load_or_init_param(name, shape):
    path = CHECKPOINT_DIR / f"{name}.npy"
    if path.exists():
        loaded = np.load(path)
        if loaded.shape == shape:
            print(f"Loaded {name} from {path}")
            return loaded.astype(np.float64)
        print(
            f"Skipping {name}: expected shape {shape}, found {loaded.shape}. Reinitializing."
        )
    return np.random.randn(*shape) * INIT_SCALE


def save_params():
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    np.save(CHECKPOINT_DIR / "embeddings.npy", embeddings)
    np.save(CHECKPOINT_DIR / "Q.npy", Q)
    np.save(CHECKPOINT_DIR / "K.npy", K)
    np.save(CHECKPOINT_DIR / "V.npy", V)
    np.save(CHECKPOINT_DIR / "W_out.npy", W_out)
    np.save(CHECKPOINT_DIR / "W_vocab.npy", W_vocab)
    np.save(CHECKPOINT_DIR / "FF2.npy", FF2)
    np.save(CHECKPOINT_DIR / "FF1.npy", FF1)
    print(f"Saved parameters to {CHECKPOINT_DIR}")


embeddings = load_or_init_param("embeddings", (vocab_size, embed_size))
Q = load_or_init_param("Q", (num_heads, embed_size, embed_size))
K = load_or_init_param("K", (num_heads, embed_size, embed_size))
V = load_or_init_param("V", (num_heads, embed_size, embed_size))
W_out = load_or_init_param("W_out", (num_heads * embed_size, embed_size))
W_vocab = load_or_init_param("W_vocab", (embed_size, vocab_size))
FF2 = load_or_init_param("FF2", (128, embed_size))
FF1 = load_or_init_param("FF1", (embed_size, 128))


def get_embeddings(word: str):
    return embeddings[vocab.index(word)]


def softmax(x):
    x = np.nan_to_num(np.asarray(x, dtype=np.float64), nan=0.0, posinf=1e6, neginf=-1e6)
    x = x - np.max(x)
    exp_x = np.exp(np.clip(x, -60, 60))
    denom = np.sum(exp_x)
    if not np.isfinite(denom) or denom <= 0:
        return np.ones_like(exp_x) / len(exp_x)
    return exp_x / denom


def layer_norm(x):
    x = np.nan_to_num(np.asarray(x, dtype=np.float64), nan=0.0, posinf=1e6, neginf=-1e6)
    mean = np.mean(x)
    std = np.sqrt(np.mean((x - mean) ** 2) + 1e-8)
    return (x - mean) / std


def cross_entropy_loss(final_probs, correct_word):
    correct_index = vocab.index(correct_word)
    correct_prob = np.clip(final_probs[correct_index], 1e-12, 1.0)
    return -np.log(correct_prob)


def clip_gradient(grad, max_val=GRAD_CLIP):
    grad = np.nan_to_num(grad, nan=0.0, posinf=max_val, neginf=-max_val)
    return np.clip(grad, -max_val, max_val)


def clip_weights(param, max_abs=WEIGHT_CLIP):
    np.clip(param, -max_abs, max_abs, out=param)


def backward(query_word, correct_word):
    global W_vocab, FF2, FF1, W_out, Q, K, V, embeddings

    final = cache["final"]
    ff2 = cache["ff2"]
    ff1 = cache["ff1"]
    projected = cache["projected"]
    combined = cache["combined"]
    raw = cache["raw"]

    d_final = final.copy()
    correct_index = vocab.index(correct_word)
    d_final[correct_index] -= 1.0
    d_final = clip_gradient(d_final)

    d_W_vocab = clip_gradient(np.outer(ff2, d_final))
    d_ff2 = clip_gradient(W_vocab @ d_final)

    d_FF2 = clip_gradient(np.outer(ff1, d_ff2))
    d_ff1 = clip_gradient(FF2 @ d_ff2)
    d_ff1[ff1 <= 0] = 0.0

    d_FF1 = clip_gradient(np.outer(projected, d_ff1))
    d_projected = clip_gradient(FF1 @ d_ff1)

    d_W_out = clip_gradient(np.outer(combined, d_projected))
    d_combined = clip_gradient(W_out @ d_projected)

    W_vocab -= LEARNING_RATE * d_W_vocab
    FF2 -= LEARNING_RATE * d_FF2
    FF1 -= LEARNING_RATE * d_FF1
    W_out -= LEARNING_RATE * d_W_out

    clip_weights(W_vocab)
    clip_weights(FF2)
    clip_weights(FF1)
    clip_weights(W_out)

    d_heads = np.split(d_combined, num_heads)

    for h in range(num_heads):
        d_head = d_heads[h]
        weights_h = cache[f"weights_{h}"]

        for i, word in enumerate(vocab):
            word_vec = get_embeddings(word)

            d_V = clip_gradient(np.outer(word_vec, weights_h[i] * d_head))
            V[h] -= LEARNING_RATE * d_V

            d_Q = clip_gradient(np.outer(raw, weights_h[i] * d_head))
            Q[h] -= LEARNING_RATE * d_Q

            d_K = clip_gradient(np.outer(word_vec, weights_h[i] * d_head))
            K[h] -= LEARNING_RATE * d_K

        clip_weights(V[h])
        clip_weights(Q[h])
        clip_weights(K[h])

    query_idx = vocab.index(query_word)
    d_embed = clip_gradient(d_combined[:embed_size])
    embeddings[query_idx] -= LEARNING_RATE * d_embed
    clip_weights(embeddings)


def train(epochs=100):
    for epoch in range(epochs):
        total_loss = 0.0
        for input_word, correct_word in training_data:
            final, prediction = attention(input_word)
            loss = cross_entropy_loss(final, correct_word)
            total_loss += loss
            backward(input_word, correct_word)

        if epoch % 10 == 0:
            print(f"Epoch {epoch} | Loss: {total_loss / len(training_data):.4f}")
        if (epoch + 1) % SAVE_EVERY == 0:
            save_params()
    save_params()


cache = {}


def attention(query_word: str):
    raw = get_embeddings(query_word).copy()
    cache["raw"] = raw

    head_outputs = []
    for h in range(num_heads):
        query = np.clip(raw @ Q[h], -1e3, 1e3)

        scores = []
        for word in vocab:
            word_key = np.clip(get_embeddings(word) @ K[h], -1e3, 1e3)
            score = np.dot(query, word_key) / np.sqrt(embed_size)
            scores.append(np.clip(score, -60, 60))

        weights = softmax(np.array(scores))
        cache[f"weights_{h}"] = weights

        output = np.zeros(embed_size, dtype=np.float64)
        for i, word in enumerate(vocab):
            word_value = np.clip(get_embeddings(word) @ V[h], -1e3, 1e3)
            output += weights[i] * word_value

        head_outputs.append(output)
        cache[f"head_{h}"] = output

    combined = np.concatenate(head_outputs)
    cache["combined"] = combined

    projected = combined @ W_out
    cache["projected"] = projected

    ff1 = np.maximum(0, projected @ FF1)
    ff1 = layer_norm(ff1)
    cache["ff1"] = ff1

    ff2 = ff1 @ FF2
    ff2 = layer_norm(ff2)
    cache["ff2"] = ff2

    final = softmax(ff2 @ W_vocab)
    cache["final"] = final

    candidate_scores = final.copy()
    best_index = int(np.argmax(candidate_scores))
    best_word = vocab[best_index]
    if best_word == query_word:
        candidate_scores[best_index] = -np.inf
        best_index = int(np.argmax(candidate_scores))
        best_word = vocab[best_index]

    return final, best_word


def chat_loop():
    print("Chat ready. Type a word from vocab. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break

        if user_input in {"exit", "quit"}:
            print("Exiting chat.")
            break

        if user_input not in vocab:
            print("Bot: I don't know that word yet. Try a word from vocab.")
            continue

        _, response = attention(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chat_loop()
