# _*_ coding : utf-8 _*_
list = [-3, -1, 1, 3, 5]

def fun():
    for i in range(len(list)):
        if list[i] == i:
            print(i)
            return
    print('-1')