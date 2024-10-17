# https://www.lanqiao.cn/problems/99/learning/?page=1&first_category_id=1
import sys

# data = '2 10\n6 5\n5 6'.splitlines()

data = sys.stdin.read().splitlines()
n, k = map(int, data[0].split())
q = []
for i in range(1, n + 1):
    h, w = map(int, data[i].split())
    q.append((h, w))

max_ = 10 ** 5


def solve():
    l, r = 1, max_
    res = r
    while r > l:
        mid = (l + r) // 2
        count = 0
        for h, w in q:
            count += (h // mid) * (w // mid)
        if count < k:
            r = mid
        else:
            res = mid
            l = mid + 1

    print(res)


solve()
