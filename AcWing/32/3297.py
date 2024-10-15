import sys
from functools import reduce

data = sys.stdin.read().splitlines()
n = int(data[0])
X = []
for i in range(n):
    X.append(reduce(lambda x, y: x * y, map(int, data[i + 1].split())))
print(max(0, sum(X)))
