n = -1
while n < 0:
    n = int(input())

acc = 0
for i in range(1, n):
    if i%3 == 0 or i%5 == 0:
        acc += i

print(acc)
