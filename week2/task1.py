s = input().strip()
a = ">>-->"
b = "<--<<"
count = 0
for i in range(len(s) - 4):
    if s[i:i+5] == a or s[i:i+5] == b:
        count += 1
print(count)