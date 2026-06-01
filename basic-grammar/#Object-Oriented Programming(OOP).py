#Object-Oriented Programming(OOP)
#类——————多个类似事物组成的群体的统称----能够帮助我们快速理解和判断事物的性质
#如 int,str,float等
#——————————————————————定义一个类  class
class Student:    #Student为类的名称(类名) 由一个或多个单词组成，每个单词的首字母大写其余小写
    native_place='海南'    #直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name=name      #self.xxx 实体属性，进行了一个赋值的操作
        self.age=age
#实例方法:定义在类的内部，第一个形参必须是self 默认参数
    def eat(self):
        print(self.name+"学生在吃饭。。。")
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
#类之外定义的称函数，类之内称为实施方法
#————静态方法 使用staticmethod进行修饰  
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰,我是静态方法')
#————类方法   使用classmethod
    @classmethod
    def cm(cls):
        print('我使用了classmethod,我是类方法')

def drink():   #定义在类之外-----函数
    print('喝水')

drink()
print(Student,type(Student),id(Student))  #类对象

#对象的创建
stu1=Student('张三',20)   #实例对象
stu2=Student('老王',21)
print(stu1,type(stu1),id(stu1))
stu1.eat()
Student.eat(stu1)
print(stu1.name,stu1.age)
print(stu1.native_place,stu2.native_place)
Student.native_place='海口'
print(stu1.native_place,stu2.native_place)
#————————————————————类方法 @classmethod   作用对象是类名
Student.cm()
#————————————————————静态方法 @staticmethod  作用对象是类名
Student.method()
#——————————————动态绑定实例对象属性
stu1.gender='男'
stu2.gender='女'
print(stu1.gender,stu2.gender)
#——————————————动态绑定方法
def show():
    print('定义在类之外的，称为函数')

stu1.show=show
stu1.show()
#stu2.show()   没为stu2定义 输出报错

#————————————————面向对象的三大特征
#----------封装  加'__'希望内部属性不在外部使用 
class Car: 
    def __init__(self,brand,weight):
        self.brand=brand
        self.__weight=weight  #前加上__则会报错外部不能引用
        print(self.brand)
    def start(self):   
        print('汽车已经启动')
    def show(self):
        print(self.brand,self.__weight)
car=Car('奔驰s480','1t')
car.start()
car.show()  #内部函数引用
print(car.brand)
# print(car.__weight) #外部不给引用
print(dir(car))
print(car._Car__weight)   #内部标识下划线可以通过dir()函数查找 然后使其显示

#------------继承
class Benz(Car):
    def __init__(self,brand,weight,price):
        super().__init__(brand,weight) #继承父类的属性和实例方法 
        #父类名称.__init__(self,参数1,参数2)
        #super(子类,self).__init__(参数1,参数2)
        self.price=price 
        print('hi')
    def __str__(self):
        return '我的品牌是{0},,价格是{1}'.format(self.brand,self.price)
    def show(self):
        print('我是son')   

car1=Benz('奔驰',"2t",13500)
print(car1.brand,car1._Car__weight,car1.price)
car1.start()
car1.show()
print(dir(car1))
print(car1)   #重写实例方法的__str__()

#----------多态     外部调用函数  
class Animal():
    def eat(self):
        print('动物在吃。。。')

class Dog(Animal):
    def eat(self):
        print('狗在吃。。。')

class Pig(Animal):
    def eat(self):
        print('猪在吃。。。')

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('人在吃。。。')

def fun(o):   #多态外部调用函数
    o.eat()


a=Person('老王',22)
b=Dog()
a.eat()
fun(a)
fun(Animal())

#——————————————————特殊属性
#x.__dict__ 获取 实例对象属性或者类的方法等
print(car1.__dict__) 
print(Animal.__dict__)
#x.__class__ 获取实例对象的类型
print(a.__class__,b.__class__)
#x.__bases__ 获取子类的父类元组   x.__base__ 同理，不过这个获取写在最前面的父辈
print(Dog.__bases__)
#x.__mro__   类的层次结构 子到父辈依次上升
print(Dog.__mro__)
#X.__subclasses__ 获取子类的列表
print(Animal.__subclasses__)

#————————————————————特殊方法
print(stu1,stu2)
s=stu1+stu2  #想相加要定义__add__ 特殊方法  或者用下面这种方法
print(s)
print(stu1.name.__add__(stu2.name)) 
print("--------------------------------------------------------------")
"""实例方法重写len()函数已获得对象的长度 如姓名几个字组成等   def __len__(self):
                                                             return len(self.xxx)"""
                                                         
Nam='张三'
print(len(Nam))
print(stu1.__len__())
#-------------__new__()
class Test(object):
    @classmethod
    def __new__(cls, *args, **kwargs):
        print("__new__ 运行，参数是 cls =", cls)
        # 真正创建对象
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("__init__ 运行，参数是 self =", self)

    @staticmethod
    def normal_static():
        print("普通静态方法运行，不需要 cls/self")

obj=Test()
Test.__new__()

class DBConnection(object):      #单例模板
    _instance=None
    def __new__(cls,*args,**kwargs):
        print("__new__被调用将DBConnection传给cls其id为{0}:".format(id(cls)))
        if cls._instance is None:
           cls._instance=super().__new__(cls)
           print('这里创建了对象id为:{0}'.format(id(cls._instance)))
        return cls._instance
    def __init__(self,host,user,pwd,db):
        print("__init__被调用,值传到self其id为:{0}".format(id(self)))
        if not hasattr(self,"inited"):
            self.host=host
            self.user=user
            self.pwd=pwd
            self.db=db
            self.inited=True
        print(f'数据库已连接:{self.host}/{self.db}')

print(f'Object这个类对象的id为:{id(object)}')
print(f'DBConnection这个类对象的id为:{id(DBConnection)}')
db1=DBConnection('localhost',"root",'123456',"test")
print(id(db1))
print(db1.__dict__)
db2=DBConnection("192.168.1.1","root","654321","prod")
print(id(db2))
print(db1 is db2)

#————————————————类的赋值与拷贝
class CPU:
    def __init__(self,Hz):
        self.Hz=Hz
    def __str__(self):
        return "我是CPU,我的赫兹是{0}".format(self.Hz)
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#---------------变量的赋值
cpu1=CPU(100)   #两变量指向同一个对象，改变其中一个对象另一个也随之改变
cpu2=cpu1
print(cpu1,cpu2,id(cpu1),id(cpu2),cpu1 is cpu2)
cpu2.Hz=200
print(cpu1.Hz,cpu2.__dict__)
#----------------浅拷贝    只拷贝源对象 不考虑子对象
disk=Disk()
computer=Computer(cpu1,disk)  
import copy #引用copy
computer2=copy.copy(computer)  #拷贝computer的属性到computer2
print(computer.__dict__)
print(computer2.__dict__)
print(id(computer),id(computer2),computer is computer2) #新建了对象但其储存的属性一样
#-----------------深拷贝   
computer3=copy.deepcopy(computer)
print(computer.__dict__)    #深拷贝 全部新建id 可以理解为另存为
print(computer3.__dict__)
print(id(computer),id(computer3),computer is computer3)