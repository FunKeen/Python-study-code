# https://www.lanqiao.cn/problems/19710/learning/?page=1&first_category_id=1

n, r = input().split()
string = ""
index = 0
for i in r:
    if i != '.':
        string += i
        index += 1
    else:
        index = 0

string = int(string) * (2 ** int(n))
string = str(string)
print(string)
if int(string[-index]) >= 5:
    print(int(string[:-index]) + 1)
else:
    print(string[:-index])
