m, h = map(float, input().split())

imc = m/h**2

if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")
