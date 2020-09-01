# put your python code here
n1 = float(input())
n2 = float(input())
hacer = input()
if hacer == "+":
    print(n1 + n2)
if hacer == "-":
    print(n1 - n2)
if hacer == "/":
    if n2 == 0:
        print("Division by 0!")
    else:
        print(n1 / n2)
if hacer == "*":
    print(n1 * n2)
if hacer == "mod":
    if n2 == 0:
        print("Division by 0!")
    else:
        print(n1 % n2)
if hacer == "pow":
    print(n1 ** n2)
if hacer == "div":
    if n2 == 0:
        print("Division by 0!")
    else:
        print(n1 // n2)