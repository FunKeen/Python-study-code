import sys

data = sys.stdin.read().splitlines()
index = 0
T = int(data[index])
index += 1
for _ in range(T):
    N, M = map(int, data[index])
    index += 1
    for _ in range(M):
        lst = list(map(int, data[index]))
        index += 1
        inCount=lst[0]

