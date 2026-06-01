#程序的组织结构
   #顺序结构 从上到下依次运行
#对象的布尔值 所有的对象都有一个布尔值 可用bool函数查看~~~~测试对象的布尔值 空值 0 none等布尔值为False
print(bool(None),bool(0),bool([]),bool(list()),bool(dict()),bool({}),bool(()))
   #选择结构 单分支结构 if xxxx:
money=1000 #余额
s=int(input('请输入你的取款金额'))
if money>=s:
    money-=s
    print('取款成功,剩余余额为',money)
else:
    print('您的余额不足，提款失败')
   #双分支结构if  else
number=int(input('请输入一个整数'))
if number%2==0:
    print(number,'是偶数')
else:
    print(number,'是奇数')
#多分支结构 if elif elif else
a=float(input('请输入您这次考试所获得的分数'))
if a>=80 and a<=100:
    print('您这次考试成绩为优秀')
elif a>=70 and a<=89:
    print('您这次考试成绩为良好')
elif a>=60 and a<=69:
    print('您这次考试成绩为及格')
elif a<=59:
    print("您这次考试不及格请多加努力")
else:
    print('您输入的成绩有误，不在有效范围内')