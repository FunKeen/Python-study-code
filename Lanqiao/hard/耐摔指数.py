import sys

n = int(input())
li = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
for index, size in enumerate(li):
    if li[index - 1] <= n < size:
        print(index)
