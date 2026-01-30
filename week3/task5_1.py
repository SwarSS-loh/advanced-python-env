def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def red(num, den):
    g = gcd(abs(num), den)
    return num // g, den // g
def sub(A, B, C, D):
    n = A * D - C * B
    den = B * D
    return red(n, den)
def main():
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))
    D = int(input("D: "))
    num, den = sub(A, B, C, D)
    print(f"Result: {num}/{den}")
if __name__ == "__main__":
    main()