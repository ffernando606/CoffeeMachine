# put your python code here

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

diferencia = (h2 - h1) * 3600
diferencia += ((m2 - m1) * 60)
diferencia += (s2 - s1)
print(diferencia)