# _*_ coding : utf-8 _*_

from re import findall

set = set()
str = input()


def fun():
    while nums:
        num = nums.pop()
        for x in nums:
            if x == num:
                print(x)
                return
    print("-1")


nums = findall(r"\d+", str)
fun()
