#1

a = int(input())
b = int(input())
s = 0
if a>b:a,b = b,a
for i in range(a, b+1):
    s += i
print(s)

#2

c = int(input())
d = int(input())
max = 1
if c>d: c,d = d,c
for j in range(c, 0, -1):
    if c%j == 0 and d%j == 0:
        max = j
    break
print(max)

#3

e = int(input())
for g in range(1, e+1):
    if e%g == 0:
        print(g, end=" ")

#4

f = int(input())
if f == 0:
    k = 1
else:
    k = 0

for h in range(f):

    if f == 0:
        break
    k += 1
    f //= 10

print(k)

#5

e = 0
ne = 0
p = 0
o = 0
i = 0
z = 0
for l in range(10):
    num_3 = int(input())

    if num_3 == 0:
        z += 1
    elif num_3 % 2 == 0:
        e += 1
    else:
        ne += 1
    if num_3 > 0:
        p += 1
    elif num_3 < 0:
        o += 1
    i += 1
print(f"положительных: {p}, отрицательных: {o}, четных: {e}, нечетных: {ne} нулей: {z}")
