# _*_ coding : utf-8 _*_
N, V = map(int, input().split())

items = []

for i in range(N):
    items.append(list(map(int, input().split())))

items = sorted(items, key=lambda x:-x[1]/x[0])

st = [0] * N

res = []
max = 0


def dp(v, val):
    global max
    if v > V:
        return
    for i in range(N):
        if st[i] == 0:
            if v + items[i][0] > V and max < val:
                max = val
                return
            else:
                st[i] = 1
                dp(v + items[i][0], val + items[i][1])
                st[i] = 0


dp(0, 0)
print(max)
