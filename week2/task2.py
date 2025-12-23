a, b = input(), input()
n = len(b)
shifts = []
for i in range(n):
    shifts.append(b[i:] + b[:i])
count = 0
for i in range(len(a)-n+1):
    if a[i:i+n] in shifts:
        count += 1
print(count)