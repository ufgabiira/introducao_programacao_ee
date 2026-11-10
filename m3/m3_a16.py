n = -1
while n < 0:
    n = int(input())

acc = 0
for i in range(1, n):
    acc += i if n%i==0 else 0

print("Sim" if n==acc else "Nao")
