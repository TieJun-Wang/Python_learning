#算数符
# +加法 -减法 *乘法 / 除法 //整除运算 %取余运算 **幂运算
print(2+2)
print(4-2)
print(2*3)
print(6/2)
print(11//5)
print(11%5)
print(2**3)
print(9//-4)  #-3
print(-9//4)  #-3
#一正一负整除运算，向下取整
print(9%-4)  #-3 余数=被除数-除数*商
print(-9%4)  #3
a=20
a*=2
print(a,type(a))
#运算符
a,b=10,20 #一一对应
print(a,b)
#进行交换 a和b的值互换 
a,b=b,a
print(a,b)
#比较运算符 结果为布尔运算符
print('a大于b吗',a>b)
print('a不等于b吗',a!=b)
#  ==比较的是value 比较标识用 is
print(a,id(a),type(a),b,id(b),type(b))
print(a is b) #比较的是id标识
# 布尔运算符 and or not
a,b=1,2
print(a==1 and b==2)
print(a==1 and b==1)
#and 需要两个都是true才能输出true否则均输入false
print(a==1 or b<2)
print(a==1 or b!=2)
print(a==2 or b==1)
# or 有一个相对于的结果为正则输出真，两个都为假才能输出false
# not 对布尔类型运算数取反
f1=False
f2=True
print(not f1)
print(not f2)
# in和not in
s='hello world'
print("h" in s)
print("e" not in s)
#位运算符 位于& 位或| 左移位运算符<< 右移位运算符>> 左移相当于乘以二 右移相当于除以二
#用于二进制比较啥的
#转化为二进制bin函数 八进制oct 十六进制 hex
print(bin(4),bin(8))
print(bin(4|8))
print(4<<2,bin(4<<2))
print(4>>1,bin(4>>1))
#运算符的优先级 算术运算(幂**，乘除取整取余，加减)  位运算(<< >> & |) 比较运算 布尔运算