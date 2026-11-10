n = int(input())
acc = 0

for i in range(1, n+1):
    acc += i if i%2 == 0 else 0

print(acc)
