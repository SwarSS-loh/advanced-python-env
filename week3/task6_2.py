import math
def tri(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def quad(a, b, c, d, diag):
    a1 = tri(a, b, diag)
    a2 = tri(c, d, diag)
    return a1 + a2
def main():
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))
    d = float(input("Side d: "))
    diag = float(input("Diagonal: "))
    print("Area:", quad(a, b, c, d, diag))
if __name__ == "__main__":
    main()