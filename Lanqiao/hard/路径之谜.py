# https://www.lanqiao.cn/problems/89/learning/?page=1&first_category_id=1&status=2
import sys
import threading

data = sys.stdin.read().splitlines()
n = int(data[0])
r = list(map(int, data[1].split()))
c = list(map(int, data[2].split()))

num = sum(r)

found = threading.Event()


def fun1():
    visited = [[0 for _ in range(n)] for _ in range(n)]

    cx = [1, 0, -1, 0]
    cy = [0, 1, 0, -1]
    sum_r = [0 for _ in range(n)]
    sum_c = [0 for _ in range(n)]

    goes = [(0, 0)]
    visited[0][0] = 1
    sum_r[0] = 1
    sum_c[0] = 1
    size = n - 1

    def go_next(x, y, step):
        sum_c[x] += 1
        sum_r[y] += 1
        goes.append((x, y))
        visited[x][y] = 1
        dfs(x, y, step)
        visited[x][y] = 0
        goes.pop()
        sum_c[x] -= 1
        sum_r[y] -= 1

    def dfs(x, y, step):
        if found.is_set():
            return
        if step > num:
            return
        if sum_c[x] > c[x] or sum_r[y] > r[y]:
            return
        if x == size and y == size:
            if sum_c == c and sum_r == r:
                for a, b in goes:
                    sys.stdout.write(f"{a * n + b} ")
                found.set()
            return
        if y == size:
            if visited[x][y - 1] == 1:
                go_next(x + 1, y, step + 1)
                return
        if x == 0 and y != 0:
            if visited[x + 1][y] == 1:
                go_next(x, y + 1, step + 1)
                return
        for i in range(4):
            dx = x + cx[i]
            dy = y + cy[i]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] != 1:
                go_next(dx, dy, step + 1)

    dfs(0, 0, 1)


def fun2():
    visited = [[0 for _ in range(n)] for _ in range(n)]

    cx = [0, 1, 0, -1]
    cy = [1, 0, -1, 0]
    sum_r = [0 for _ in range(n)]
    sum_c = [0 for _ in range(n)]

    goes = [(0, 0)]
    visited[0][0] = 1
    sum_r[0] = 1
    sum_c[0] = 1
    size = n - 1

    def go_next(x, y, step):
        sum_c[x] += 1
        sum_r[y] += 1
        goes.append((x, y))
        visited[x][y] = 1
        dfs(x, y, step)
        visited[x][y] = 0
        goes.pop()
        sum_c[x] -= 1
        sum_r[y] -= 1

    def dfs(x, y, step):
        if found.is_set():
            return
        if step > num:
            return
        if sum_c[x] > c[x] or sum_r[y] > r[y]:
            return
        if x == size and y == size:
            if sum_c == c and sum_r == r:
                for a, b in goes:
                    sys.stdout.write(f"{a * n + b} ")
                found.set()
            return
        if x == size:
            if visited[x - 1][y] == 1:
                go_next(x, y + 1, step + 1)
                return
        if y == 0 and x != 0:
            if visited[x][y + 1] == 1:
                go_next(x + 1, y, step + 1)
                return
        for i in range(4):
            dx = x + cx[i]
            dy = y + cy[i]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] != 1:
                go_next(dx, dy, step + 1)

    dfs(0, 0, 1)


thread1 = threading.Thread(target=fun1)
thread2 = threading.Thread(target=fun2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
