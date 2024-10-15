import sys

data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())

mem = [tuple()] * (n + 1)
res = 0

for i in range(1, n + 1):
    temp = tuple(map(int, data[i].split()))
    mem[i] = temp

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            isc = True
            for k in range(m):
                if mem[i][k] >= mem[j][k]:
                    isc = False
                    break
            if isc:
                res = j
                break
            else:
                res = 0
    print(res)
