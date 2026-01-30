def sort(word):
    return "".join(sorted(word))
def trans(s):
    words = s.split()
    return " ".join(sort(w) for w in words)
def main():
    s = input("Enter string: ")
    print(trans(s))
if __name__ == "__main__":
    main()