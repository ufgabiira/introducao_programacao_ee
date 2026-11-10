def tensao(adc):
    return adc*5/1023

def para_motor(v):
    return v*100/5

def saturar(pp):
    if pp < 0:
        return 0
    elif pp > 80:
        return 80
    return pp

adc = int(input())
pot_percent_sat = saturar(para_motor(tensao(adc)))
print(f"motor: {round(pot_percent_sat)}%")
