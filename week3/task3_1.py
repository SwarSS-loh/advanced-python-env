import math
def htp(a, b):
    return math.sqrt(a**2 + b**2)
def main():
    a1 = float(input("Triangle1 leg a: "))
    b1 = float(input("Triangle1 leg b: "))
    a2 = float(input("Triangle2 leg a: "))
    b2 = float(input("Triangle2 leg b: "))
    h1 = htp(a1, b1)
    h2 = htp(a2, b2)
    print("Hyp1:", h1)
    print("Hyp2:", h2)
    if h1 > h2:
        print("First hypotenuse is greater")
    elif h2 > h1:
        print("Second hypotenuse is greater")
    else:
        print("Hypotenuses are equal")
if __name__ == "__main__":
    main()