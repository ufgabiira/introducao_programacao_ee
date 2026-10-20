qtd, valor_und = input().split()
qtd = int(qtd)
valor_und = float(valor_und)
v_total = qtd * valor_und

if qtd >= 100:
    v_total = v_total * 0.8
elif qtd >= 50:
    v_total = v_total * 0.9
elif qtd >= 10:
    v_total = v_total * 0.95

print(f"{v_total:.2f}")
