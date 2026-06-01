#循环结构
#while 四步循环法
a=1
sum=0
while a<101:
    if not bool(a%2):
        sum+=a
    a+=1
print('和为',sum)
# for in 循环
for i in range(2,101,2):
    print(i)
for _ in range(3):
     print(list(range(3)),"hello world")
ss=0
for item in range(2,101,2):
    if not bool(item%2):
        ss+=item
print(ss)
#水仙花数 100到999
for item in range(100,1000):
    a=item%10
    b=item//10%10
    c=item//100
    if a**3+b**3+c**3==item:
     print(item)
#斐波那契数列
a,b=0,1
while b<1000:
    a,b=b,a
    b+=a
    print(b)