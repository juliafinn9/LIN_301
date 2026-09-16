import re                                                     # loads Python's regex toolkit

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string, called `text`

matches_not_ao = re.findall(r"c[^ao]t", text)   # finds "cat", "cot", or "cut"
print(len(matches_not_ao))                      # counts how many were found
print(*matches_not_ao, sep="\n")                # prints each match on a separate line