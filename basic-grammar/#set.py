#set
#————————集合的创建  可以理解成无value的字典  集合的元素不允许重复 只能放不可变序列
s={'python',123}
print(s,type(s))
print(set((1,2,3,4,5)))
s1=set(range(1,11,2))
print(s1,type(s1))
#定义空集合
s2=set()
print(s2,type(s2))
#—————————集合中的相关操作
s3={10,20,30,40,50,'python','hello',(1,2,3,4,5)}
print(s3)
print('python' in s3)
#—————————集合元素的添加
s3.add(80)   #------添加单个add
print(s3)
s3.update({60,70,80})   #------添加多个update 可以添加列表 集合 元组 等
print(s3)
#——————————集合元素的删除  remove---不存在会异常 discard------不存在不会报错  pop()-----随机删除一个 clear()----清空
s3.remove(80)
print(s3)
s3.discard(10)
print(s3) 
#——————————集合之间的关系
#-------==或!=判断是否相等
s11=set(range(1,11,2))
s12=set(range(2,11,2))
print(s11)
print(s12)
print(s11==s12)
t=tuple((2,4,6,8,10))
s11.update(t)
print(s11)
#-------子集判断 xxx.issubset(yyy)  x是y的子集吗
print(s11.issubset(s12))
print(s12.issubset(s11))
#-------超集判断  x.issupersety   x是y的超集吗
print(s11.issuperset(s12))
#-------交集判断  x.isdisjoint(y) x y两个集合是否没有交集 
print(s11.isdisjoint(s12))
print(not s11.isdisjoint(s12))       #两个集合是否有交集
#——————————集合的数学操作
#---------交集操作 x.intersection()或者x & Y 
s111={1,3,5,7,9}
s222={2,4,6,8,10}
print(s111.intersection(s222))
print(s111 & s222)
#----------并集操作 x.union() x | y
print(s111.union(s222))
print(s111 | s222)
#----------差集操作 x.difference(y)  x - y
s111.add(10)
print(s111)
print(s111.difference(s222))
#----------对称差值(相当于并集减去差值) x.symmetric_difference()  x ^ y
print(s111.symmetric_difference(s222))
print(s111 ^ s222)
#——————————集合的生成式
set1={i*i for i in range(1,11)}
print(set1)