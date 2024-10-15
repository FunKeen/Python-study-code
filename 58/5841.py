# _*_ coding : utf-8 _*_
import sys

a, b, c = map(int, sys.stdin.read().split())

if a == b + c or b == a + c or c == a + b:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")
