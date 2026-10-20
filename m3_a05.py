n = 0

while n < 1:
    n = int(input())

count = 0

for i in range(1, n+1):
    count += 1 if n%i==0 else 0

print(count)
