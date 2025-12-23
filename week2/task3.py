a = input()
if a[0] == 'x':
    x = int(a[4]) - int(a[2]) if a[1] == '+' else int(a[4]) + int(a[2])
elif a[2] == 'x':
    x = int(a[4]) - int(a[0]) if a[1] == '+' else int(a[0]) - int(a[4])
else:
    x = int(a[0]) + int(a[2]) if a[1] == '+' else int(a[0]) - int(a[2])
print(x)
