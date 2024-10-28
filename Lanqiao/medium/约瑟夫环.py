# https://www.lanqiao.cn/problems/231/learning/?page=2
n, k = map(int, input().split())
result = 0
for i in range(2, n + 1):
    result = (result + k) % i
print(result + 1)
