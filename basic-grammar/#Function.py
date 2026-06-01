#Function
#————————函数的创建
def calc(a,b):  #a和b为形式参数简称形参-----定义处
    c=a+b  #c称为局部变量 可用global去变成全局变量
    return c

result=calc(10,20)   #实际参数的值简称实参-----调动处
res=calc(b=10,a=20)  #关键字参数 根据形参名称进行实参传递
print(result,res)

#——————————函数的内存分析
def fun(arg1,arg2):
    print('agr1',arg1)
    print("arg2",arg2)
    arg1+=100
    arg2.append(10)
    print('arg1',arg1)
    print('agr2',arg2)

n1=11
n2=[22,33,44]
print(n1)
print(n2)
print("--------")
fun(n1,n2)
print(n1)
print(n2)
#------在函数的调用过程中，进行参数的传递
#如果是不可变对象，在函数体内的修改不会影响实参的值
#如果是可变对象，会影响到实参的值
#——————————函数的返回值
def fun1(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst1=[i for i in range(100,111,1)]
print(fun1(lst1))  
#-----返回值-----
#(1)如果函数没有返回值[函数执行完毕后，不需要给调用处提供数据]  return可省略不写
#(2)函数的返回值如果是一个直接返回类型
#(3)函数的返回值如果是多个，返回结果为元组
"""————————————函数的形参设置——————————"""
#函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
def fun3(a,b=10):   #b为默认值参数
    print(a,b)

fun3(100)      #-----只传一个参数，b采用默认值
fun3(20,30)    #-----30将默认值10替换
#-------个数可变的位置参数和关键字参数  定义新函数的时候无法事先确定传递的位置实参的个数时
def f1(*args):     #可变的位置参数 输出的是元组 只能定义一个
    print(args[0],args[-1])
    print(args[0]+args[-1])

f1(10,20,40,59,214,214,24)

def f2(**args):    #个数可变的关键字形参 输出的是字典 只能定义一个
    print(args)

f2(a=10)
f2(a=10,b=20,c=30)
#调用时也可用通过加*实现
#---------在一个函数的定义过程中 个数可变的位置形参放在个数可变的关键字形参之前-----------

def f3(a,b,*,c,d,**args):  #星号*后面只能写入关键字形参
    print('a=',a)
    print('b=',b)
    print('c',c)
    print('d=',d)
    print(args)

f3(10,20,c=30,d=49,e=100)
#def f(a,b=10,*args,**args)  先位置形参再到关键字形参
'''————————————————————————'''
#————————————变量的作用域
def f4(a,b):
    c=a+b    #局部变量   体外直接输出会报错
    print(c)

name='elisa'
def f5():
    print(name)

f5()
def f6():
    global age    # 使用global使局部变量变为全局变量
    age=22
    print(age)

f6()
print(age)
#——————————————递归函数
def ff(n):
    if n==1:
        return 1
    else:
        res1=n*ff(n-1)
        return res1
    
print(ff(6))

#斐波那契数列(1000以内)
a,b=0,1
while b<1000:
    a,b=b,a
    b+=a
    print(a,end=' ')
print()
#递归思想
def function(n):   #第n位的斐波那契数列
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return function(n-1)+function(n-2)
        
print(function(4))
for i in range(1,7):
    print(function(i),end=" ")  #前六项数列的数字
print()
def fuc(n):   #计算第五个孩子的年龄 每个孩子都比前一个孩子岁数多1
    if n==1:
        return 10
    else:
        return fuc(n-1)+2
        
print(fuc(5))

#爬楼梯问题------需要n阶你才能到达楼顶每次可以爬一步或者两步，有多少种方法
def climb_stairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climb_stairs(n-1)+climb_stairs(n-2)
print("-------")
print(climb_stairs(10))