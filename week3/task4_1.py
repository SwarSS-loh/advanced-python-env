def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def red(num, den):
    g = gcd(num, den)
    return num // g, den // g
def div(A, B, C, D):
    num = A * D
    den = B * C
    return red(num, den)
def main():
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))
    D = int(input("D: "))
    num, den = div(A, B, C, D)
    print(f"Result: {num}/{den}")
if __name__ == "__main__":
    main()