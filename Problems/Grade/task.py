grade = float(input())
top = int(input())
if grade >= top * .9 and grade <= top:
    print("A")
if grade >= top * .8 and grade < top * .9:
    print("B")
if grade >= top * .7 and grade < top * .8:
    print("C")
if grade >= top * .6 and grade < top * .7:
    print("D")
if grade < top * .6:
    print("F")