import math
classroom = [0, 0, 0, 0]
for i in range(0, 3):
    classroom[i] = int(input())
    classroom[i] = (math.ceil(classroom[i]/2))
    classroom[3] += classroom[i]
print(classroom[3])


