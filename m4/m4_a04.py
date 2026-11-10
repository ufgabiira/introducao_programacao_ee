def mapear(x, de_min, de_max, para_min, para_max):
    return para_min + (x - de_min)/(de_max - de_min)*(para_max - para_min)

f_origem = list(map(float, input().split()))
f_destino = mapear(*f_origem)

print(f"{f_destino:.2f}")
