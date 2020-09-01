def calc():
    halls = int(input())
    capacity = int(input())
    viewers = int(input())
    if ((halls * capacity) >= viewers):
        return True
    else:
        return False


a = calc()
print(a)
