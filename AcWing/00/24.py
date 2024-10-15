# _*_ coding : utf-8 _*_
# k, m, n = input().split()
k, m, n = 18, 40, 40

f = lambda x: sum([int(i) for i in str(x)])

count = 0

st = []

for i in range(m):
    st.append([0] * n)


def dfs(x, y):
    global count
    if (0 <= x < m and 0 <= y < n) and st[x][y] == 0:
        if f(x) + f(y) <= k:
            count += 1
        st[x][y] = 1
        dfs(x + 1, y)
        dfs(x, y + 1)


dfs(0, 0)
print(count)
