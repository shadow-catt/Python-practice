import random
secret = random.randint(0,9)
print("——————猜数字——————")
a = 3
print("0~9之间哦")
while a>0:
    print("剩余机会：%d"%a)
    sb = input('猜猜我在想那个数字:\n')
    guess=int(sb)
    if guess==secret:
        print("牛批，你猜对了")
        break
    else:
        if guess<secret:
            print("小了哟")
        else:
            print("大了哟")
        if a>1:
            print("再猜一次吧~\n\n")
        else:
            print("抱歉，宁的机会用完啦。。。\n")
            print("其实我心里想的数字是%d"%secret)
    a=a-1
print("游戏结束，感谢宁的游玩")
    
