# https://www.lanqiao.cn/problems/152/learning/?page=1&first_category_id=1&second_category_id=3&tags=%E6%9A%B4%E5%8A%9B&tag_relation=intersection
import sys

n = int(input())
a, b, c = map(int, input().split())
st = [True] * (n + 1)

for i in [a, b, c]:
    index = i
    st[index] = False
    while True:
        index += i
        if index > n:
            break
        st[index] = False

print(sum([1 for i in st[1:] if i]))
