n = input()
i = int(n)
acc = 0

while i != 0:
    acc += (i%10)**len(n)
    i = i // 10

print("Sim" if acc == int(n) else "Nao")
