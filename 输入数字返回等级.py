#方法一
"""利用elif函数进行分支"""

score=int (input("请输入一个分数：\n"))
if 100>=score>=90:
    print("A")
elif 90>score>=80:   #else if(条件)
    print("B")
elif 80>=score>=70:
    print("C")
elif 70>=score>=60:
    print("D")
elif 60>score>=0:
    print("E")
else:
    print("你输错啦")


'''if和else之间的关系看缩进'''
