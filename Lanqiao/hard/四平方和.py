# https://www.lanqiao.cn/problems/122/learning/?page=2&first_category_id=1&second_category_id=3
import sys

n = int(input())
mem = {}
for i in range(2237):
    mem[i * i] = i
s = mem.keys()


def solve():
    for i in s:
        for j in s:
            for k in s:
                l = n - i - j - k
                if l in mem:
                    print(mem[i], mem[j], mem[k], mem[l])
                    return


solve()
