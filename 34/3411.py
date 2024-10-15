import sys

data = sys.stdin.read().split()
n, m, l = map(int, data[:3])

res = {i: 0 for i in range(l)}

for x in data[3:]:
    res[int(x)] += + 1

print(*res.values())
