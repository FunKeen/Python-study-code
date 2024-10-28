import sys
from copy import deepcopy

data = [5160, 9191, 6410, 4657, 7492, 1531, 8854, 1253, 4520, 9231, 1266, 4801, 3484, 4323, 5070, 1789, 2744, 5959,
        9426, 4433, 4404, 5291, 2470, 8533, 7608, 2935, 8922, 5273, 8364, 8819, 7374, 8077, 5336, 8495, 5602, 6553,
        3548, 5267, 9150, 3309]

S = sum(data)
data.sort()
arr = []
max_ = 0


def dfs(x):
    global max_
    if x >= 40:
        a = sum(arr)
        if a == 113462:
            print(a)
        return
    dfs(x + 1)
    arr.append(data[x])
    dfs(x + 1)
    arr.pop()


dfs(0)
print(113462 ** 2)
