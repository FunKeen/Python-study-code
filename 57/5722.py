# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().splitlines()
c, m, n = map(int, data[0].split())
C = []
p = []
for i in range(1, m + 1):
    x, w = map(int, data[i].split())
    C.append((i - 1, x, w))

C.sort(key=lambda x: x[1])
X = [0] * m
W = [0] * m
st = [1] * m
for i in range(m):
    X[i] = C[i][1]
    W[i] = C[i][2]


def erf(n):
    l, r = 0, m - 1
    mid = (l + r) // 2
    while r >= l:
        mid = (l + r) // 2
        if X[mid] == n:
            return mid
        if X[mid] < n:
            l = mid + 1
        else:
            r = mid


for i in range(m + 1, m + n + 1):
    p.append(int(data[i]))
for i in p:
    q = [i]
    while q:
        x = q.pop()
        temp = erf(x)
        W[temp] += 1
        if W[temp] > 4:
            st[temp] = 0
            m -= 1
            index = temp + 1
            while index < m:
                if st[index] == 1:
                    if W[index] == 4:
                        q.append(X[index])
                    break
                index += 1
            index = temp
            while index > 0:
                index -= 1
                if st[index] == 1:
                    if W[index] == 4:
                        q.append(X[index])
                    break
        print(q)
    print(m)
