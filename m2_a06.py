a, b, c = map(int, input().split())

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("invalido")
elif a == b and b == c:
    print("equilatero")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("escaleno")
