# https://www.lanqiao.cn/problems/118/learning/?page=2&first_category_id=1&second_category_id=3
import sys

m, n = map(int,sys.stdin.read().split())
sum = m + n
arr = [0]

res = 0


def dfs(a, b, li):
    global res
    if a > m or b > n:
        return
    if a == m and b == n:
        res += 1

    def fun(ta, tb, new_li):
        for i in li:
            if i == 'A':
                if i == new_li[-1]:
                    ta += 1
                    new_li.append('A')
                else:
                    tb += 1
                    new_li.append('B')
            elif i == 'B':
                if i == new_li[-1]:
                    ta += 1
                    new_li.append('A')
                else:
                    tb += 1
                    new_li.append('B')
        dfs(ta, tb, new_li)

    fun(a + 1, b, ['A'])
    fun(a, b + 1, ['B'])


dfs(1, 0, ['A'])
dfs(0, 1, ['B'])

print(res)
