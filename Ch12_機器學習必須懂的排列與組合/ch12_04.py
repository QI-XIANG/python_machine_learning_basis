import math

N = 30
times = 10000000000000
day_secs = 24 * 60 * 60
year_secs = 365 * day_secs
combinations = math.factorial(30)
years = combinations / times / year_secs
print("需要 %d 年才可以獲得結果" % years)