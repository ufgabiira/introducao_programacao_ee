n = 0

while n < 1:
    n = int(input())

fib = "0"
a, b = 0, 0

for i in range(1, n):
    if b == 0:
        fib += " 1"
        b = 1
    else:
        temp = a + b
        fib += f" {temp}"
        a = b
        b = temp

print(fib)
