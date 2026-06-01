#内置函数 range(start，stop，step) 
r=range(1,10,2)  #左闭右开 无指定则默认步长为1 起始数字为0
print(r)
print(list(r))
print(9 in r) #判断数字是否在序列中
#水仙数
for item in range(100,1000):
    a=item%10
    b=item//10%10
    c=item//100
    if a**3+b**3+c**3==item:
     print(item)
i=100
while i<1000:
    a1=i%10
    b2=i//10%10
    c3=i//100
    if a1**3+b2**3+c3**3==i:
     print(i)
    i+=1 
   