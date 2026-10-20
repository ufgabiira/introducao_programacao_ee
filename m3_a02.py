n = 0
while n <= 0:
    n = int(input())

nums = map(int, input().split())
even = 0
odd = 0

for i in nums:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print(f"Pares: {even}\nImpares: {odd}")
