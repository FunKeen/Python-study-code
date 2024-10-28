import sys

n=20230610

sum=0
hight=1
count=1

while sum<=n:
    sum+=count
    hight+=1
    count+=hight
print(hight-2)