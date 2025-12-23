def count(seq):
    a1 = '>>-->'
    a2 = '<--<<'
    count = 0 
    count += seq.count(a1)
    count += seq.count(a2)
    return count
a = input()
b = count(a)
print(b)
