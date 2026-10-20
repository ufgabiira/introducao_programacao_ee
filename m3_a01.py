n = int(input())
big = n

while n != -1:
    if big < n:
        big = n
    n = int(input())

print(big)
