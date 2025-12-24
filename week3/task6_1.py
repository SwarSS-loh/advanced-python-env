def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
def main():
    A = int(input("A: "))
    B = int(input("B: "))
    print("GCD:", gcd(A, B))
    print("LCM:", lcm(A, B))
if __name__ == "__main__":
    main()