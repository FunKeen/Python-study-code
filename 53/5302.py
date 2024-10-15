# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().splitlines()
dict = {}
n = int(data[0])

a, b = 1, n + 1
for i in range(a, b):
    s, a = data[i].split()
    dict[s] = a
m = int(data[n + 1])

a, b = n + 2, n + m + 2
for i in range(a, b):
    q = data[i]
    if q in dict:
        sys.stdout.write(f'{dict[q]}\n')
    else:
        sys.stdout.write('-1\n')
