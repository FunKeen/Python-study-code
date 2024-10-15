# _*_ coding : utf-8 _*_

from re import findall

# str = input("Enter a string: ")

str = "[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]"

list = [1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15]


def fun(list, n):
    mid = len(list) // 2
    print(list[mid])
    print(list[:mid])
    print(list[mid + 1:])
    if list[mid] == n:
        return mid
    # if len(list) == 1:
    #     return None
    if list[mid] > n:
        fun(list[:mid], n)
    else:
        fun(list[mid + 1:], n)


print(fun(list, 6))
