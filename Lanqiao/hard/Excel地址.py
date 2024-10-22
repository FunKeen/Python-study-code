# https://www.lanqiao.cn/problems/96/learning/?page=1&first_category_id=1&second_category_id=3
import sys

n = int(input())
str = 'ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Map = {i: str[i] for i in range(27)}
stack = []
while n > 0:
    temp = n % 26
    stack.append(Map[temp])
    n = (n - 1) // 26
[sys.stdout.write(i) for i in stack[::-1]]
