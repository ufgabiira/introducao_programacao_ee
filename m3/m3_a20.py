n = -1
while n < 0:
    n = int(input())

acc = 0
i = 0
while n!=0:
    acc += (n%10) * 2**i
    n = n // 10
    i += 1

print(acc)
