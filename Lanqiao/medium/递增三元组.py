# https://www.lanqiao.cn/problems/172/learning/?page=5&first_category_id=1
import sys

# data = sys.stdin.read().splitlines()
data = ['3', '1 1 1', '2 2 2', '2 3 3']
n = int(data[0])
a = list(map(int, data[1].split()))
b = list(map(int, data[2].split()))
c = list(map(int, data[3].split()))
a.sort()
c.sort()


def erfa(x):
    l, r = 0, n
    while r > l:
        mid = (l + r) // 2
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid
    return r


def erfc(x):
    l, r = 0, n
    while r - l >= 1:
        mid = (l + r) // 2
        if c[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return r


count = 0
for i in b:
    A = erfa(i)
    C = n - erfc(i)
    if A == 0 or C == 0:
        continue
    count += A * C

print(count)
