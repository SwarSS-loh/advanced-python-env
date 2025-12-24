import math
def tri(a):
    h = a * math.sqrt(3) / 2
    return a * h / 2
def hex(a):
    return 6 * tri(a)
def main():
    a = float(input("Side of regular hexagon: "))
    print("Area:", hex(a))
if __name__ == "__main__":
    main()