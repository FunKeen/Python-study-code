# _*_ coding : utf-8 _*_

res = {1: '2(0)', 2: '2', 3: '2+2(0)', 4: '2(2)',
       5: '2(2)+2(0)', 6: '2(2)+2', 7: '2(2)+2+2(0)'}


def main(n):
    try:
        return res[n]
    except KeyError:
        str = ''
        for i in range(15, 0, -1):
            if 2 ** i - n < 0:
                print(i)
                str += main(2 ** i)
        res[n] = str
        return res[n]


def func(n, res):
    while n % 2:
        res.append(n % 2)
        n //= 2
    return res[::-1]


print(func(8, []))
