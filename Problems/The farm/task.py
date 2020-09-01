guita = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
if guita < 23:
    print(None)
if 23 <= guita < 678:
    if guita // chicken >= 2:
        print(f"{guita // chicken} chickens")
    else:
        print(f"{guita // chicken} chicken")
if 678 <= guita < 1296:
    if guita // goat >= 2:
        print(f"{guita // goat} goats")
    else:
        print(f"{guita // goat} goat")
if 1296 <= guita < 3848:
    if guita // pig >= 2:
        print(f"{guita // pig} pigs")
    else:
        print(f"{guita // pig} pig")
if 3848 <= guita < 6769:
    if guita // cow >= 2:
        print(f"{guita // cow} cows")
    else:
        print(f"{guita // cow} cow")
if guita >= 6769:
    print(f"{guita // sheep} sheep")
