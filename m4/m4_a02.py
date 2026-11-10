def em_serie(r1, r2):
    return r1 + r2

def em_paralelo(r1, r2):
    return r1*r2/(r1+r2)

r1, r2 = map(float, input().split())
r_serie = em_serie(r1, r2)
r_paralelo = em_paralelo(r1, r2)

print(f"Serie: {r_serie:.2f}\nParalelo: {r_paralelo:.2f}")
