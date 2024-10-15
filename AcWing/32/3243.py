# _*_ coding : utf-8 _*_
n = int(input())
m = int(input())
do = []
for i in range(m):
    do.append(list(map(int, input().split())))

no = [i for i in range(1, n + 1)]

for d in do:
    index = no.index(d[0])
    insert = no.pop(index)
    no.insert(index+d[1], insert)

[print(x,end=' ') for x in no]
