a, b = -1, -1
while a < 0 or b < 0:
    a, b = map(int, input().split())

c, d = a, b

while b != 0:
    a, b = b, a%b

mmc = (c * d)//a

print(mmc)
