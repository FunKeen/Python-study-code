# https://www.lanqiao.cn/problems/130/learning/?page=2&first_category_id=1&second_category_id=3
w, m, n = map(int, input().split())

rowm = (m - 1) // w
rown = (n - 1) // w


def getcol(row, num):
    if row % 2 == 0:
        col = (num - 1) % w
    else:
        col = w - (num - 1) % w - 1
    return col


print(abs(getcol(rowm, m) - getcol(rown, n)) + abs(rowm - rown))
