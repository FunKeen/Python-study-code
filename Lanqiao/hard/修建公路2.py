# https://www.lanqiao.cn/problems/1125/learning/?page=1&first_category_id=1&second_category_id=8
import sys
from Myclass.UnionFind import UnionFind

# data = sys.stdin.read().splitlines()
data = ['5 6', '1 2 2', '1 3 7', '1 4 6', '2 3 1', '3 4 3', '3 5 2']
n, m = map(int, data[0].split())

if n == 1 and m == 0:
    print(0)
    sys.exit()

sorted_edges = []

[sorted_edges.append(list(map(int, str.split()))) for str in data[1:m + 1]]
sorted_edges.sort(key=lambda x: x[2])

edge_size = n - 1


def kru():
    uf = UnionFind(n)
    mts = []
    for a, b, val in sorted_edges:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            mts.append((a, b, val))
        if len(mts) >= edge_size:
            break
    return mts


mst = kru()
min_ = float('inf')
for i in mst:
    uf = UnionFind(n)
    temp_mst = []
    res = 0
    for a, b, val in sorted_edges:
        if (a, b, val) == i:
            continue
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            temp_mst.append((a, b, val))
            res += val
        if res > min_:
            continue
        if len(temp_mst) >= edge_size:
            break
    if len(temp_mst) >= edge_size:
        min_ = min(min_, res)
print(min_)
