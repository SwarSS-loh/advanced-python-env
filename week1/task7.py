o = input("Choose your operation between +, -, *, /: ")
n1 = int(input("num1: "))
n2 = int(input("num2: "))
if o == "+":
    print(n1 + n2)
elif o == "-":
    print(n1 - n2)
elif o == "*":
    print(n1 * n2)
elif o == "/":
    if n2 == 0:
        print("You cannot divide by 0")
    else:
        print(n1 / n2)
