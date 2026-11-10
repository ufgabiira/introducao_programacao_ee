def divisor_tensao(vin, r1, r2):
    return vin*r2/(r1+r2)

vout = divisor_tensao(*list(map(float, input().split())))
print(f"{vout:.2f}")
