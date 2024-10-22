import sys

Map = []
for i in range(3):
    Map.append(list(map(int, input().split())))
st = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        if Map[i][j] == 0:
            pass
        else:
            st[i][j] += 1
over = True
while over:
    over = False
    for i in range(3):
        for j in range(3):
            r = sum(st[i])
            c = sum([st[k][j] for k in range(3)])
            if r == 2 or c == 2:
                st[i][j] = 1
                over = True
            else:
                if i == j:
                    d1 = st[0][0] + st[1][1] + st[2][2]
                    if d1 == 2:
                        st[i][j] = 1
                        over = True
                elif i + j == 3:
                    d2 = st[0][2] + st[1][1] + st[2][0]
                    if d2 == 2:
                        st[i][j] = 1
                        over = True

print(st)
