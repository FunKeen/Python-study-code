# https://www.lanqiao.cn/problems/102/learning/?page=2&first_category_id=1

start = list(input())
end = list(input())

state = [-3, -2, -1, 1, 2, 3]
size = len(start)

mem = {tuple(start): 0}


def bfs(x, y):
    q = [(x, start, y)]
    while q:
        step, l, index = q.pop(0)
        for di in state:
            i = index + di
            if 0 <= i < size and l[i] != l[index]:
                l[index], l[i] = l[i], l[index]
                if l == end:
                    print(step + 1)
                    return
                temp = l.copy()
                if tuple(temp) in mem:
                    pass
                else:
                    mem[tuple(temp)] = 0
                    q.append((step + 1, temp, i))
                l[index], l[i] = l[i], l[index]


bfs(0, start.index('*'))
