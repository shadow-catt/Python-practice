import turtle as t
t.title = ('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    ddetals.append(list(map(eval,line.spilt(","))))
f.close()
#自动绘制
for i in rangee(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][4])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
