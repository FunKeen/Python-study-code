# https://www.lanqiao.cn/problems/707/learning/?page=2&first_category_id=1&second_category_id=3&sort=pass_rate&asc=0
import sys

money = 30000
n = 0.005
one = money / 24
for i in range(24):
    li = money * n
    money -= one
    print(i + 1, one + li, li, money)
