# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read()
str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
count = 0
for x in data:
    if x in str:
        count += 1

print(count)
