# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().splitlines()
index = 0
while True:
    n, m, k = map(int, data[index].split())
    for_list = list(range(index+1, index+k + 1))
    index += k + 1

    dict = []
    num = {(i, j): 0 for i in range(0, n) for j in [0, 1]}

    for i in for_list:
        id, x, y = map(int, data[i].split())
        if x == 0 or y == 0:
            continue
        num[(x, 0)] += 1
        num[(y, 1)] += 1
        dict.append([x, y])

    # dict.sort(key=lambda x: (x[0], x[1]))
    # for i in dict:
    #     print(i)

    count = 0

    while dict:
        ma = max(num.items(), key=lambda x: x[1])
        temp = []
        for x in dict:
            if x[ma[0][1]] != ma[0][0]:
                temp.append(x)
            else:
                num[(x[0], 0)] -= 1
                num[(x[1], 1)] -= 1
        dict = temp
        count += 1

    print(count)
    if int(data[index][0]) == 0:
        break
