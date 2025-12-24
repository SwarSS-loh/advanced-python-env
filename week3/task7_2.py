def oct(n):
    oct_str = format(n, "o")
    return oct_str.zfill(10)
def main():
    n = int(input("Non-negative integer: "))
    print(oct(n))
if __name__ == "__main__":
    main()