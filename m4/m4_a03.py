def tensao(adc):
    return adc*5/1023

print(f"{tensao(float(input())):.2f}")
