def euclid_extended(a, b):
    if b == 0:
        return a, 1, 0



    d, x, y = euclid_extended(b, a % b)

    return d, y, x - y * (a // b)

a = 11
b = 10

d, x, y = euclid_extended(a, b)
print(f"a={a}, b={b}, НОД={d}")
print(f"{x}*{a} + {y}*{b} = {d}")