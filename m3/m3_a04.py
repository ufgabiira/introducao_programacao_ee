n = 0
acc = 0
count = 0

while True:
    num = float(input())
    if num != -1:
        acc += num
        count += 1
    else:
        break

med = acc/count
print(f"{med:.2f}")
