# https://www.lanqiao.cn/problems/718/learning/?page=2&first_category_id=1&second_category_id=3&sort=pass_rate&asc=0

for i in range(10, 100):
    str1 = str(i ** 3)
    str2 = str(i ** 4)
    string = str1 + str2
    if len(str1) == 4 and len(str2) == 6 and all(str(x) in string for x in range(0, 10)):
        print(i)
