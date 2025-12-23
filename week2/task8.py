s1 = input().strip()
s2 = input().strip()
from collections import Counter
if Counter(s1) == Counter(s2):
    print("YES")
else:
    print("NO")