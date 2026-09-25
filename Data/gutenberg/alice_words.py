with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string called `text`

text_split = text.split()
print(text_split[:1000])

tokens = len(text_split)
types = len(set(text_split))

ttr = types/tokens
print(ttr)