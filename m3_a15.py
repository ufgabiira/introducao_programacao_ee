a, b = -1, -1
while a < 0 or b < 0:
    a, b = map(int, input().split())

while b != 0:
    a, b = b, a%b

print(a)
