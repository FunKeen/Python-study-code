# https://www.lanqiao.cn/problems/2080/learning/?page=1&first_category_id=1&status=2
import sys

data = sys.stdin.read().splitlines()
n = int(data[0])
l = list(map(int, data[1].split()))
d = list(map(int, data[1].split()))
res=0

for i in range(1, n):
    d[i] += d[i - 1]
for i in range(n-1):
    res += l[i] * (d[- 1] - d[i])
print(res)
