import sys

data = list(sys.stdin.read().replace('\n', ''))

mem = {'0': 0, '1': 0}
for i in data:
    if i in mem:
        mem[i] += 1

min_val = 10 * 8
for key, val in mem.items():
    min_val = min(min_val, val)
print(min_val)
print(list(reversed(data)))
