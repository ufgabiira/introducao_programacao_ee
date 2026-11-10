n1, n2, n3 = map(int, input().split())
maior = 0

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior = n2
else:
    maior = n3

print(maior)
