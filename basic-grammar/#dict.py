#scores=  dict()
#字典 用花括号定义 {} 是可变数列可以进行增删改但里面的元素都是不可变序列如字符串str 以键值对进行存储
#原理是计算hash函数找到对应的value
#————————字典的创建——————————
scores={'张三':100,'李四':200,'王五':300}
print(scores)
a=dict(name="张三",age=20)
print(a)
print(a.keys())
#————————获取字典键的值 dict[]  dict.get()
print(scores['张三'])
print(scores.get('王五'))
print(a.get('name'),a.get('age'))   #——————get(xxxx，yyy)的方法查找的值不存在则会输出None(yyy) 另一种则为报错
#——————————字典的增删改
#-----判断 in  not in
b='张三' in scores
print('张三'in scores)
print(b)
#------删除指定的键值对 del dict[]
print(scores)
del scores['张三']
print(scores)
scores.clear()  #清空字典
print(scores)
#-------新增键值对
scores['张三']=100
print(scores)
#-------修改键值对
scores['张三']=200
print(scores)
#——————————获取字典视图 keys() values() items()  得到的是集合
aa={'张三':111,'李四':222,'老王':333}
print(aa.keys())
print(aa.values())
print(aa.items())
print(list(aa.keys()))
print(list(aa.items()))  # 元组组成
#———————————字典的遍历
for i in aa:    #-----获取的是字典里的键的值
    print(i,aa[i],aa.get(i))
#———————————字典的特点 key：value,  key不可重复 value可以重复
#                                   字典的元素是无序的
#———————————字典生成式 zip()
items=['Fruits','Books','Others']
prices=[96,78,85]
d={items.upper():prices   for items,prices in zip(items,prices) }
print(d)
print(d.items())
print(d.keys())
print(d.values())