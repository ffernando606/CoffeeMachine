number = int(input())
word = input()

# write a condition for plurals

if number != 1:
    print(f"{str(number)} {word}s")
else:
    print(f"{str(number)} {word}")
