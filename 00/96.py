# _*_ coding : utf-8 _*_
res2 = {1: 1, 2: 3}
res1 = {1: 1, 2: 3}


def fun(num):
    try:
        return res2[num]
    except KeyError:
        keys = res2.keys()
        re = [fun(i) + fun2(j) for i in keys for j in keys if i + j == num - 1]
        res2[num] = 2 * min(re) + 1
        return res2[num]


def fun2(num):
    try:
        return res1[num]
    except KeyError:
        res1[num] = 2 * fun2(num - 1) + 1
        return res1[num]


[print(fun(i)) for i in range(1, 13)]
