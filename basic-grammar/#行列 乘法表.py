#输出一个三行四列的矩形
for i in range(1,4):
    for j in range(1,5):
        print("$",end='\t') #不换行输出
    print()  #打行
#直角三角形
for a in range(1,10):
    for b in range(1,a+1):
        print(a,'*',b,'=',a*b,end="   ")
    print()