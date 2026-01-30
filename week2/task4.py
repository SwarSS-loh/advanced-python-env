a, b = map(int, input().split())
text = input().strip()
s = set()
for i in range(a - b + 1):
    s.add(text[i:i+b])
print(len(s))