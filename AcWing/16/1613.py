import sys
from copy import deepcopy
import datetime

# start_time = datetime.datetime.now()

# data = '52...6...\n......7.1\n3........\n...4..8..\n6......5.\n.........\n.418.....\n....3..2.\n..87.....'.splitlines()
data = sys.stdin.read().splitlines()
Map = [list(x) for x in data]

nums = set(map(str, range(1, 10)))


def dfs(funMap):
    def getdict():
        def bfun(x, y):
            bx = x // 3 * 3
            by = y // 3 * 3
            return [funMap[bx + i][by + j] for i in range(3) for j in range(3)]

        def fun(x, y):
            l = funMap[x]
            c = [funMap[x][y] for x in range(9)]
            q = bfun(x, y)
            return [x, y, sorted(list(nums - set(l + c + q)))]

        return [fun(i, j) for i in range(9) for j in range(9) if funMap[i][j] == "."]

    while True:
        dict = getdict()
        sortedbylen = sorted(dict, key=lambda x: -len(x[2]))
        if not sortedbylen:
            for i in funMap:
                [sys.stdout.write(x) for x in i]
                sys.stdout.write('\n')
            # end_time = datetime.datetime.now()
            # print(end_time - start_time)
            # sys.exit()
        elif len(sortedbylen[-1][2]) > 1:
            x, y, temp = sortedbylen.pop()
            for item in temp:
                newmap = deepcopy(funMap)
                newmap[x][y] = item
                dfs(newmap)
            break
        else:
            ed = []
            while sortedbylen:
                x, y, temp = sortedbylen.pop()
                templen = len(temp)
                if templen == 0:
                    return
                elif templen == 1 and temp[0] not in ed:
                    ed.append(temp[0])
                    funMap[x][y] = temp[0]
                else:
                    break


dfs(Map)
