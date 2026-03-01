# Chatty MC — 2,616 Parameters

Chatty MC 2,600 is our first huge step up from autocompletion. 
Trained on a small dataset, this model can output single words only.

This model has slight context understanding through pattern matching. 
It is an architecture model — not meant to be perfect, just a stepping stone 
in the Chatty MC series.

## Model Info
ARC = Transformer (Multi-Head Attention)
PARAMETERS = 2,616
HEADS = 3
EMBED SIZE = 8
VOCAB SIZE = 51
EPOCHS = 4000
FINAL LOSS = ~2.93

## Chatty MC Series
- Chatty MC 160     → No attention, nweighted list proximity
- Chatty MC 800     → Single head attention, no training
- Chatty MC 2,616   → Multi-head attention, backpropagation 

## How to Run
pip install numpy
python ai.py

## Word Limitations
[
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
