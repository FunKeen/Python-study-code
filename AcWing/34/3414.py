import sys

data = sys.stdin.read().split()
n = int(data[0])
size = int(data[-1])
b = list(map(int, data[1:]))

b = [0] + b if b[-1] != 0 else b

dp = [0 for _ in range(n + 1)]

for i in range(1, len(b)):
    dp[i] = dp[i - 1]
    leng1 = b[i] - b[i - 1]
    print(b[i - 1], b[i])
    k = 1
    for j in range(2, leng1):
        if (leng1) % j == 0:
            k += 1
    if i == 1:
        dp[i] = k
    else:
        count = 0
        for j in range(2, b[i]):
            if b[i] % j == 0:
                if all(x % j != 0 for x in b[1:i]):
                    count += 1
        print(b[1:i], k, count)
        dp[i] = dp[i] * k + count
print(*dp)
print(dp[len(b) - 1])
