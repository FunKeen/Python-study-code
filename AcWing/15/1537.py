# _*_ coding : utf-8 _*_
n = int(input())
list = list(map(int, input().split()))

list = sorted(list)

arr = [0] * n
st = [0] * n


def dfs(x):
    if x == n:
        print(*arr)
        return
    le = len(list)
    for i in range(le):
        if st[i] == 0:
            st[i] = 1
            arr[x] = list[i]
            dfs(x + 1)
            arr[x] = 0
            st[i] = 0


dfs(0)
