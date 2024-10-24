# https://www.lanqiao.cn/problems/2297/learning/?page=2&first_category_id=1&second_category_id=3&sort=pass_rate&asc=0
import datetime

t = datetime.datetime.strptime('2022-1-1', '%Y-%m-%d') - datetime.datetime.strptime('1949-10-1', '%Y-%m-%d')
print(t.days)