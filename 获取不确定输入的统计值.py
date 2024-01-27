def getNum():       #获取用户不定长度的输入
    Num_ = input()
    Num  =list(eval(Num_))
    return Num
def mean(numbers):  #计算平均值
    s=0.0
    for i in numbers:
        s=s+i
    return s/len(numbers)
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)
def median(numbers):    #计算中位数
    size = len(numbers)
    print(s)
    print(numbers)
    if size%2==0:
        return (numbers[size//2-1]+numbers[size//2])/2
    else:
        return numbers[size//2]
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
