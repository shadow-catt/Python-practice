x,y = 4,5
if x<y:
    small = x
else:
    small = y
print("4和5之间的最小值为：\n%d" %small)

x,y=6,7
big = x if x > y else y
print("6和7之间的最大值为：\n%d" %big)


#可以简化为
#small = x if x < y else y
#x if 条件 else y

