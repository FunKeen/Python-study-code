# https://www.lanqiao.cn/problems/106/learning/?page=1&first_category_id=1&second_category_id=3

str = input().strip()
stack = []

for x in str:
    if x in ['(', 'x', '|']:
        stack.append(x)
    elif x == ')':
        temp = []
        while True:
            out_ = stack.pop()
            if out_ == '(':
                break
            temp.append(out_)
        max_len = max(map(len, (''.join(temp).split('|'))))
        stack += ['x'] * max_len
    else:
        pass
max_len = max(map(len, (''.join(stack).split('|'))))
print(max_len)
