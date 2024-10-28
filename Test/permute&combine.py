def permute(s):
    result = []
    stack = [(s, '')]

    while stack:
        s, path = stack.pop()
        if not s:
            result.append(path)
        else:
            for i in range(len(s)):
                stack.append((s[:i] + s[i + 1:], path + s[i]))

    return result


print(permute("abc"))


def combine(n, k):
    result = []
    stack = [(1, [])]

    while stack:
        start, path = stack.pop()

        if len(path) == k:
            result.append(path)
            continue

        for i in range(start, n + 1):
            stack.append((i + 1, path + [i]))

    return result


print(combine(4, 2))
