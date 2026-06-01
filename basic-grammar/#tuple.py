#tuple
#元组的创建
t=("world",98,"hello")
print(type(t))
tt=tuple(('hello','world','human'))
t1=(1,)  #——————只有一个元素必须加逗号
print(t1)
t3=('hello',[100,200,300,400],123,{'张三':100,'李四':200,'王五':300})
print(t3[1],type(t3[1]))
t3[1].append(500)
print(t3[1])
print(t3[-1])
t3[-1]['张三']=150
print(t3[-1])
#——————————元组的遍历
for g in t3:
    print(g)