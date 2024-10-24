# mem = {1: 1, 2: 2, 3: 16, 7: 52, 15: 160, 27: 9232, 255: 13120, 447: 39364, 639: 41524, 703: 250504, 1819: 1276936,
#        4255: 6810136, 4591: 8153620, 9663: 27114424, 20895: 50143264, 26623: 106358020, 31911: 121012864,
#        60975: 593279152, 77671: 1570824736, 113383: 2482111348, 138367: 2798323360, 159487: 17202377752,
#        270271: 24648077896, 665215: 52483285312, 704511: 56991483520}
# mem = {1: 1, 2: 2, 3: 16, 7: 52, 15: 160, 27: 9232, 255: 13120, 447: 39364, 639: 41524, 703: 250504, 1819: 1276936,
#        4255: 6810136, 4591: 8153620, 9663: 27114424, 20895: 50143264, 26623: 106358020, 31911: 121012864,
#        60975: 593279152, 77671: 1570824736, 113383: 2482111348, 138367: 2798323360, 159487: 17202377752,
#        270271: 24648077896, 665215: 52483285312, 704511: 56991483520}

# n = int(input())
# res = mem[1]
# for key, val in mem.items():
#     if n == key:
#         print(val)
#         break
#     elif n > key:
#         res = val
#         continue
#     elif n < key:
#         print(res)
#         break

# mem = {}
# max_ = 0
# for i in range(1, 10 ** 4):
#     max_1 = 0
#     temp = i
#     while temp != 1:
#         max_ = max(temp, max_)
#         max_1 = max(temp, max_1)
#         if temp % 2 == 0:
#             temp //= 2
#         else:
#             temp = temp * 3 + 1
#     print(i, max_, max_1)
#     if max_1 == max_ and max_1 not in mem.values():
#         mem[i] = max_1
# for i in mem.items():
#     print(i)

mem = {1: 1, 2: 2}

n = int(input())
max_ = 1
for i in range(1, n):
    temp = i
    max_ = max(temp, max_)
    while temp != 1:
        if temp < i:
            break
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = temp * 3 + 1
        if temp > max_:
            mem[i] = temp
            max_ = temp
print(max_)
