def classificar(adc):
    if adc < 341:
        return "baixo"
    elif adc < 682:
        return "medio"

    return "alto"

print(classificar(int(input())))
