al = set("ABCEHKMOPTXY")
def vbhrekvnrejk(s):
    if len(s) != 6:
        return False
    if s[0] not in al:
        return False
    if not (s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
        return False
    if s[4] not in al or s[5] not in al:
        return False
    return True
n = int(input())
for i in range(n):
    plate = input().strip()
    print("Yes" if vbhrekvnrejk(plate) else "No")