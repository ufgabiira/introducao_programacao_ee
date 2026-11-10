n = -1
while n < 0:
    n = int(input())

bin = ""
if n == 0:
    bin += '0'

while n!=0:
    bin = str(n%2) + bin
    n = n // 2

print(bin)
