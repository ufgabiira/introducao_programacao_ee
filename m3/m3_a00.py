n = 0
while n<1:
    n = int(input())

qtd = 0
nums = []
while qtd != n:
    nums = list(map(int, input().split()))
    qtd = len(nums)

sum = 0
for i in nums:
    sum += i

print(sum)
