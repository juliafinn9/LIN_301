import re                                                     # loads Python's regex toolkit

with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:  # opens alice.txt for reading
    text = f.read()                                           # reads the whole file into one string, called `text`

matches = re.findall(r"c.t", text)   # finds every match of "c_t"
print(len(matches))                  # counts how many were found -- this matches grep -Eo's count
print(*matches, sep="\n")            # prints each match on a separate line