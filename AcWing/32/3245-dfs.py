# _*_ coding : utf-8 _*_

n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

# 排序，让bfs优先选择权值较小的边
edges = sorted(edges, key=lambda x: x[2])

minre = 99999999
goes = []
mem = [99999999] * (n + 1)


def bfs(x, d):
    print(x, d)
    global minre
    if d >= minre:
        return
    if x == n:
        minre = min(minre, d)
        return
    try:
        edges[x]
    except KeyError:
        return
    goes.append(x)
    for a, b, c in edges:
        if a == x and b not in goes:
            bfs(b, max(d, c))
        if b == x and a not in goes:
            bfs(a, max(d, c))
    goes.pop()


bfs(1, 0)
print(minre)
