def print(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
def main():
    n = int(input("Number: "))
    print(n)
if __name__ == "__main__":
    main()