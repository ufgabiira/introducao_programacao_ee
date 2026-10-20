num = "-1"
while int(num) < 0:
    num = input()

invert = ""
length = len(num)
num = int(num)

for i in range(length):
    invert += str(num%10)
    num = num // 10

print(int(invert))
