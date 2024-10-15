# _*_ coding : utf-8 _*_
import sys

data = sys.stdin.read().splitlines()
a, b, c, d = map(int, data)

ans = (a + b) * (c - d)
sys.stdout.write(f"ANSWER = {ans}")
