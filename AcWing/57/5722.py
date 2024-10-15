# _*_ coding : utf-8 _*_
import sys

data = '30 30 38\n10 1\n23 1\n16 2\n12 1\n14 4\n3 1\n17 3\n15 3\n22 2\n19 1\n11 2\n18 2\n13 2\n1 1\n6 3\n25 3\n8 1\n2 2\n21 2\n5 1\n28 3\n26 1\n20 1\n9 2\n7 3\n29 2\n24 4\n4 4\n30 3\n27 2\n6\n5\n22\n30\n18\n17\n12\n13\n24\n22\n10\n12\n29\n1\n27\n19\n12\n23\n15\n17\n23\n14\n10\n26\n19\n2\n1\n2\n1\n28\n22\n6\n4\n1\n9\n5\n28\n27\n'
data = data.splitlines()
# data = sys.stdin.read().splitlines()
c, m, n = map(int, data[0].split())
C = []
p = []
for i in range(1, m + 1):
    x, w = map(int, data[i].split())
    C.append([x, w, 1])

C.sort(key=lambda x: x[0])

t = m

for i in range(m + 1, m + n + 1):
    p.append(int(data[i]))

boom = {}


def erf(n):
    l, r = 0, t
    while r > l:
        mid = (l + r) // 2
        if C[mid][0] == n:
            return mid
        elif C[mid][0] < n:
            l = mid + 1
        else:
            r = mid


for i in p:
    q = [i]
    while q:
        x = q.pop()
        temp = erf(x)
        C[temp][1] += 1
        if C[temp][1] > 4:
            C[temp][2] = 0
            m -= 1
            index = temp + 1
            while index < t:
                if C[index][2] == 1:
                    C[index][1] += 1
                    if C[index][1] > 4 and C[index][0] not in boom:
                        boom[C[index][0]] = 0
                        q.append(C[index][0])
                    break
                index += 1
            index = temp
            while index > 0:
                index -= 1
                if C[index][2] == 1:
                    C[index][1] += 1
                    if C[index][1] > 4 and C[index][0] not in boom:
                        boom[C[index][0]] = 0
                        q.append(C[index][0])
                    break
    sys.stdout.write(f"{m}\n")
