import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
y = set()
yr0 = []
yr1 = []
for i in range(n):
    a, b = map(int, data[i + 1].split())
    y.add(a)
    if b == 0:
        yr0.append(a)
    else:
        yr1.append(a)

yr0 = sorted(yr0)
yr1 = sorted(yr1)

len1 = len(yr1)


def erf(list, n):
    l, r = 0, len(list)
    while r - l >= 1:
        mid = (l + r) // 2
        if list[mid] < n:
            l = mid + 1
        else:
            r = mid
    return r


res = []
for item in y:
    s = erf(yr0, item) + len1 - erf(yr1, item)
    res.append([item, s])

print(max(res, key=lambda x: (x[1], x[0]))[0])
