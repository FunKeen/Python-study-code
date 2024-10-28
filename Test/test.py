a, b, n = map(int, input().split())


def quick_pow_mod(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result


print(a * quick_pow_mod(10, n + 2, 0) % 1000)
