def ins(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 <= R**2
def main():
    a = float(input("Circle center x: "))
    b = float(input("Circle center y: "))
    R = float(input("Radius R: "))
    points = {}
    for name in ["P", "F", "L"]:
        x = float(input(f"{name} x: "))
        y = float(input(f"{name} y: "))
        points[name] = (x, y)
    count = 0
    for name, (x, y) in points.items():
        if ins(x, y, a, b, R):
            count += 1
    print("Points inside circle:", count)
if __name__ == "__main__":
    main()