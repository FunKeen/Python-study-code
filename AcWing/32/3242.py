# _*_ coding : utf-8 _*_
n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

ks = 0
for i in a:
    ks += i
    if ks >= k:
        count += 1
        ks = 0
if ks != 0:
    count += 1

print(count)
