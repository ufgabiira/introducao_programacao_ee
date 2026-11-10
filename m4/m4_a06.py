def menor_de(a, b):
    return min([a, b])

i1, i2, i3 = map(int, input().split())
print(menor_de(i1, menor_de(i2, i3)))
