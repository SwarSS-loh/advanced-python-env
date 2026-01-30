def sum(arr):
    s = sum(arr)
    avg = s / len(arr) if arr else 0
    return s, avg
def read(n):
    a = int(input(f"Size of array {n} (<=15): "))
    a = min(a, 15)
    arr = []
    for i in range(a):
        arr.append(int(input(f"{n}[{i}]: ")))
    return arr
def main():
    arrays = []
    for i in range(1, 4):
        arrays.append(read(f"A{i}"))
    for i, arr in enumerate(arrays, start=1):
        s, avg = sum(arr)
        print(f"Array A{i}: sum = {s}, avg = {avg}")
if __name__ == "__main__":
    main()