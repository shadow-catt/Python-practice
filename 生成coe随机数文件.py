import random
file1="randomNumber.coe"
fp=open(file1,"w+")

testtime,radix=eval(input("输入你要测试的乘法组数a以及以什么进制输出b的: (128,10)\n"))

if(radix==16):
    replace="hex"
elif(radix==2):
    replace="bin"
elif(radix==10):
    replace="int"
elif(radix==8):
    replace="oct"


testtimes=testtime*2
a=[0 for i in range(testtimes)]

fp.write("MEMORY_INITIALIZATION_RADIX={};\n".format(radix))
fp.write("MEMORY_INITIALIZATION_VECTOR=\n")

for i in range(testtimes):
    a[i]=random.getrandbits(128)
    fp.write(str(eval(replace)(a[i]))[2:])
    if(i%2==1 and  i !=testtimes-1):
        fp.write("\n")


fp.seek(0)
for line in fp:
    print(line)

fp.close()
