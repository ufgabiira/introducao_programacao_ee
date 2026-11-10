n = 0

while n<=0:
    n = int(input())

original = n
invertido = 0

while n >= 1:
    invertido = (invertido * 10) + n%10
    n = n // 10

if invertido == original:
    print("palindromo")
else:
    print("nao palindromo")
