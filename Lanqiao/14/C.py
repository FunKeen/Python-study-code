import sys
from collections import defaultdict

data = sys.stdin.read().strip()
dict = defaultdict(int)
for i in data:
    dict[i] += 1
for key, val in dict.items():
    if val % 2 != 0:
        print('NO')
        sys.exit()
    else:
        continue
print('YES')
