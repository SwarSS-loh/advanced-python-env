import string
from collections import Counter
def analyze(input="text.txt", output="analysis.txt"):
    with open(input, "r", encoding="utf-8") as f:
        lines = f.readlines()
    line = len(lines)
    words = []
    table = str.maketrans("", "", string.punctuation)
    for line in lines:
        line = line.lower().translate(table)
        words.extend(line.split())
    wordscou = len(words)
    freq = Counter(words)
    with open(output, "w", encoding="utf-8") as out:
        out.write(f"Total lines: {line}\n")
        out.write(f"Total words: {wordscou}\n")
        out.write("Word frequencies:\n")
        for word, count in freq.most_common():
            out.write(f"{word}: {count}\n")
if __name__ == "__main__":
    analyze()