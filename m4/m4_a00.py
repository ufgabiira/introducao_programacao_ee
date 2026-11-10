def potencia(v, i):
    return v*i

tens, corr = map(float, input().split())
print(f"{potencia(tens, corr):.2f}")
