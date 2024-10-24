li = [0, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def erf(lst, n):
    l, r = 0, len(lst)
    while r > l:
        mid = (l + r) // 2
        if lst[mid] < n:
            l = mid + 1
        else:
            r = mid
    return r


print(erf(li, 6))
print(erf(li, 7))
print(erf(li, 8))
print(len(li) - erf(li, 8))
