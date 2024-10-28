x = 343720
y = 233333


def fun(x):
    return x / 15 * 17


for i in range(1, 1000000):
    if fun(i * x) % y == 0:
        a = fun(x * i) ** 2 + (x * i) ** 2
        print(f"{a ** 0.5 * 2:.2f}")
        break
