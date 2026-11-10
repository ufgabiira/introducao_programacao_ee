n = -1
while n < 0:
    n = int(input())

acc = 0
while n != 0:
    acc += 1
    n = n // 10

print(acc)
