n1 = int(input())
n2 = int(input())
border = [1, 8]
if (n1 in border) and (n2 in border):
    print(3)
elif n1 in border or n2 in border:
    print(5)
else:
    print(8)