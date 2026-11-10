n = int(input())

prime = True

for i in range(2, n):
    if n%i==0:
       prime = False

print("true" if prime else "false")
