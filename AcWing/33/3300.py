import sys

data = sys.stdin.read().splitlines()
n, m, k = map(int, data[0].split())
t = []
road = []
for_list = list(range(1, 1 + n))
for i in for_list:
    t.append(list(map(int, data[i].split())))

for_list = list(range(1 + n, n + n))
for i in for_list:
    road.append(list(map(int, data[i].split())))

T = {i: [] for i in range(k)}
T0 = []
for i in range(n):
    if sum(t[i]) == 0:
        T0.append(i)
    for j in range(len(t[i])):
        if t[i][j]:
            T[j].append(i)
print(T)
print(T0)
