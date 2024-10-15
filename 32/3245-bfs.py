# _*_ coding : utf-8 _*_

n, m = map(int, input().split())
dict = {}
for i in range(1, n + 1):
    dict[i] = {}
for i in range(m):
    u, v, val = map(int, input().split())
    dict[u][v] = val
    dict[v][u] = val

res = []


def bfs(start, d):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(visited)
            for key, value in dict[vertex].items():
                if key not in visited:
                    queue.append(key)


bfs(1, 0)
print(res)
