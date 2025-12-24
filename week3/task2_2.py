def rec(a, b):
    return a * b
def main():
    for i in range(1, 4):
        a = float(input(f"Rectangle {i} side a: "))
        b = float(input(f"Rectangle {i} side b: "))
        print(f"Rectangle {i} area:", rec(a, b))
if __name__ == "__main__":
    main()