import os
import re
import pandas as pd

HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/

def ttr(words):
    return len(set(words)) / len(words)

def ttr_first(words, n=10000):
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    total = 0
    for w in words:
        total += len(w)
    return total / len(words)

def load_text(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()

    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]

    return "".join(lines)

def load_words(filename):
    text = load_text(filename)
    words = re.split(r"[\W_]+", text.lower())
    return [w for w in words if w != ""]

def report(title, words):
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    return ttr_first(words)

def ly_rate(words):
    total = 0
    for w in words:
        if w.endswith("ly"):
            total += 1
    return total / len(words) * 1000