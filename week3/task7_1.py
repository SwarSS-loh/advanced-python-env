def right(x, y):
    return x * y / 2
def rec(z, t):
    return z * t
def main():
    X = float(input("X: "))
    Y = float(input("Y: "))
    Z = float(input("Z: "))
    T = float(input("T: "))
    area = right(X, Y) + rec(Z, T)
    print("Quadrilateral area:", area)
if __name__ == "__main__":
    main()