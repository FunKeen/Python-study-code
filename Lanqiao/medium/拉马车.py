# https://www.lanqiao.cn/problems/101/learning/?page=1&first_category_id=1
import sys

A = list(input())
B = list(input())

table = []


def do_A():
    if B:
        if A[0] in table:
            temp = A[0]
            A.append(A.pop(0))
            while True:
                out_ = table.pop()
                A.append(out_)
                if out_ == temp:
                    break
            do_A()
        else:
            table.append(A.pop(0))
            do_B()
    else:
        for i in A:
            print(i, end="")
        print()


def do_B():
    if A:
        if B[0] in table:
            temp = B[0]
            B.append(B.pop(0))
            while True:
                out_ = table.pop()
                B.append(out_)
                if out_ == temp:
                    break
            do_B()
        else:
            table.append(B.pop(0))
            do_A()
    else:
        for i in B:
            print(i, end="")
        print()


do_A()
