# https://www.lanqiao.cn/problems/1124/learning/?page=1&first_category_id=1&second_category_id=8
import sys
import heapq
from Myclass.UnionFind import UnionFind
from collections import defaultdict

# data = sys.stdin.read().splitlines()
data = ['5 6', '1 2 2', '1 3 7', '1 4 6', '2 3 1', '3 4 3', '3 5 2']
n, m = map(int, data[0].split())

if n == 1 and m == 0:
    print(0)
    sys.exit()

# edges = defaultdict(dict)
try:
    sorted_edges = []
    for str in data[1:m + 1]:
        a, b, c = map(int, str.split())
        # edges[a][b] = c
        # edges[b][a] = c
        heapq.heappush(sorted_edges, (c, a, b))

    # def prim(startpoint):
    #     queue = []
    #     res = 0
    #     vis = set()
    #     vis.add(startpoint)
    #     for end, val in edges[startpoint].items():
    #         heapq.heappush(queue, (val, end))
    #     while queue:
    #         if len(vis) >= n:
    #             break
    #         val, end = heapq.heappop(queue)
    #         if end in vis:
    #             continue
    #         else:
    #             res += val
    #             vis.add(end)
    #             for start, val in edges[end].items():
    #                 if start not in vis:
    #                     heapq.heappush(queue, (val, start))
    #     if len(vis) >= n:
    #         return res
    #     else:
    #         return -1

    edge_size = n - 1


    def kru(startpoint):
        uf = UnionFind(n)
        mts = []
        res = 0
        while sorted_edges:
            if len(mts) >= edge_size:
                break
            val, a, b = heapq.heappop(sorted_edges)
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                res += val
                mts.append((a, b))
        if len(mts) >= edge_size:
            return res
        else:
            return -1


    print(kru(int(data[1][0])))
except:
    print(-1)
