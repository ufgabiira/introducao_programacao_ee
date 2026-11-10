def saturar(v, min, max):
    if v < min:
        return min
    elif v > max:
        return max
    return v

v, min, max = map(int, input().split())
print(f"{saturar(v, min, max)}")
