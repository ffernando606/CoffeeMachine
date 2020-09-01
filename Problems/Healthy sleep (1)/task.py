a = int(input())
b = int(input())
h = int(input())
if a <= b:
    if h < a:
        print("Deficiency")
    elif h > b:
        print("Excess")
    else:
        print("Normal")
