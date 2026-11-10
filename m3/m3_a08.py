n = int(input())
acc = 0

while True:
    if n != 0:
        acc += n%10
        n = n // 10
    else:
        break

print(acc)
