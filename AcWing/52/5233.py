# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().strip().split('\n')
print(data)
list = list(map(float, data))
print(f'{len([i for i in list if i < 0])} negative numbers')
