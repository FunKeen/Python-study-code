import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
max_ = max(data)
res = [1] * (max_ + 1)
res[1] = 0
for i in range(2, max_ + 1):
    for j in range(2 * i, max_ + 1, i):
        res[j] = 0

for i in data[1:]:
    print(res[i])

# def is_prim(x):
#     if x == 1:
#         return 0
#     elif x == 2:
#         return 1
#     elif x % 2 == 0:
#         return 0
#     for i in range(3, int(x ** 0.5) + 1, 2):
#         if x % i == 0:
#             return 0
#     return 1
#
#
# for i in data[1:]:
#     sys.stdout.write(f"{is_prim(i)}\n")
