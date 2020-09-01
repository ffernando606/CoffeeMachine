hora = int(input())
n = 10.5 + hora
if n > 24:
    print("Wednesday")
elif n < 0:
    print("Monday")
else:
    print("Tuesday")
