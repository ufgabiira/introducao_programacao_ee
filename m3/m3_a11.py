n = -1
while n < 0:
    n = int(input())

fib = 0
prev = 0
curr = 1
i = 2
while True:
    if n == 0:
        fib = prev
        break
    elif n == 1:
        fib = curr
        break
    elif i > n:
        break
    else:
        fib = prev + curr
        prev = curr
        curr = fib
        i += 1

print(fib)
