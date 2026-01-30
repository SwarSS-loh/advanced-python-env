a = input().split()
f = {}
for i in a:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print("Purchase frequency:")
for i in f:
    print(i, f[i])