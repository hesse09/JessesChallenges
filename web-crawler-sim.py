documents: dict = {
    1: "Python is a powerful programming language",
    2: "Python is great for data science and AI",
    3: "Machine learning uses Python and statistics",
    4: "Cooking pasta requires boiling water",
    5: "Artificial intelligence and machine learning are the future",
}


def sanitize(docs: dict) -> dict:
    for k, v in docs.items():
        docs[k] = v.lower()

    return docs


def crawl(cleaned_docs: dict) -> dict:
    index: dict = {}
    for k, v in cleaned_docs.items():
        tokenList = v.split(" ")
        for t in tokenList:
            if t in index:
                index[t].add(k)
            else:
                index[t] = {k}

    return index


cleaned = sanitize(documents)
final = crawl(cleaned)

print(final)
