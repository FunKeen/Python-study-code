# _*_ coding : utf-8 _*_
res = {2: 1, 3: 2, 4: 4, 5: 6}
for i in range(6, 60):
    m = 0
    for j in range(2, (i // 2) + 1):
        tm = max(j * (i - j), res[j] * res[i - j], res[j] * (i - j), j * res[i - j])
        if tm > m:
            m = tm
    res[i] = m
n=int(input())
print(res[n])
