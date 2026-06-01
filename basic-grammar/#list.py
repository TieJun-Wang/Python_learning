#lst
'''方括号[]定义列表,中间用逗号间隔'''
lst1=['hello','world',98,'hardworking']
'''使用内置函数list'''
lst2=list(['hello','world',98])
print(lst1)
print(lst2)
print(lst1[0])
'''列表获取索引 lst.index(xxxx,1,3)'''  # 1,3  表示在(1,3)中寻找索引 
print(lst1.index('hello')) #如果列表中有相同元素返回第一个相同的
print(lst1.index('hardworking'))
print(lst1.index('world',1,3))
'''获取列表多个元素 切片操作'''
lst3=[10,20,30,40,50,60,70,80]
print(lst3[1:6:1])   #新切的列表为新id [start：stop：step]
print(lst3[1:6:2])
print(lst3[-1:-5:-1])  #元素个数等于start-stop的差除以步长然后向下取整
#列表的判断 用not和not in判断   遍历 用for in 依次输出列表的数据
print(10 in lst3)
for item in lst3:
    print(item,end=' ')
#列表的添加——————lst.append(xxx)(在末尾添加一个元素，添加之后列表ID不变)
#————————lst.extend(lstxx)------列表末尾依次添加多个元素 相当于扩充 可以扩充另一个表格
#————————list.insert(索引,xxx)  -------在指定索引前(负数)位添加元素
lst3.insert(1,15)
print(lst3)
print(lst1)
#   lst4=lst3[1:5:1]
#   print(lst4)
#   lst4.extend(lst1)
#   print(lst4)
#直接操作切片后添加
lst3[4:]=lst1
print(lst3)
#lst的删除操作
#——————lst.remove() 从列表中移除一个元素 如果有重复元素移除第一个
lst4=[10,10,20,30,40,50,60]
print(lst4)
lst4.remove(10)
print(lst4)
#———————lst.pop()  根据索引移除元素  不写参数则默认删除最后一个元素
lst4.pop(0)
print(lst4)
#———————切片操作
lst4[1:3]=[]  #————————用空列表替代
print(lst4)
#————————lst.clear() 清除列表所有元素
#————————del lst 删除列表对象指代
#———————列表元素的修改 lst[索引]=xxx
lst5=[10,20,30,40,50]
print(lst5)
lst5[1]=200
print(lst5)
lst5[1:3:1]=[15,20,25,30,35]  #多个替代
print(lst5)
#————————列表的排序操作 sort
lst00=[20,49,58,44,25]
print(lst00)
lst00.sort()  #默认升序 不改变列表id  sort(reverse=True) 则表示降序
print(lst00)
#————————使用函数sorted()进行排序 将产生新的列表 sorted(lst,reverse=True) 则表示降序
lst11=[14,4,214,54,675,75,12,42]
New_lst=sorted(lst11)
print(lst11)
print(New_lst)
desc_lst=sorted(lst11,reverse=True)
print(desc_lst)
#————————列表生成式 
lst22=[i for i in range(2,11,2)]
print(lst22)
print(len(lst22))  #len()函数可以用于判断列表中的元素个数
lst222=[123]
lst222.clear()
print(lst22)
print(len(lst22))
a=0
lst_judge=[]
while a==0:
    lst_judge.clear()
    test1=float(input('Test请输入一个数字'))
    for i in range(1,11,2):
        if i==test1:
            lst_judge.append(i)
    if len(lst_judge)==0:
        a+=1
    else:
        print('执行循环操作')
        print(lst_judge)