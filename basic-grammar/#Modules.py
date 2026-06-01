#Modules
#一个模块当中可以包含函数，类(包含类属性，实例方法，类方法等)，语句等
#python程序又有n多个模块
#自定义模块 .py的文件 名称尽量不要与python自带的标准模块名称相同
'''————————————导入模块 import 模块名称 as 别名
                from 模块名称 import 函数/变量/类'''
import math #只想导入模块里的某个 例子:from math import pi——————————只导入math中的pi
print(dir(math))  #dir()函数查看模块里有何物
print(math.e)   # e的值
print(math.pi)  # π的值
print(math.log(1,math.e))  #对数写法，以math.e为底计算、
print(math.log10(10))
print(0>math.inf)
print(math.floor(3.6))  #floor向下取整
print(math.pow(2,3),type(math.pow(2,3)))  #pow(n,m)输出n的m次方
#——————————————————以主程序形式运行
try:
    import Str
except BaseException as e:
    print('错误类型是:',e)

#if __name__=='__main__': 以主程序方式运行 (只有当运行本py时才会用，导入到别的模块无法使用)
print("—"*50)
#————————————————python中的包
#python---n个包---n个模块
#包package中包含__init__.py的模块 而目录directory没有
#import package_name.modules_name as xxx(别名)
#from package_name.modules.name import function
#————————————————————————常见的内置模块  
#--------sys
import sys
print(sys.getsizeof(36))   #获取对象的内存大小单位byte
#--------time
import time
print(time.time())   #获取秒数
print(time.localtime(time.time()))   #将获取的秒数转化为具体表示时间
import calendar as cadar
print(cadar.isleap(1984))
#--------urllib-----爬虫时候运用
from urllib.request import urlopen as op
#print(op('http://www.baidu.com').read())
#--------json 用于使用json序列化和反序列化对象
#--------re 用于字符串中执行正则表达式匹配和替换
#--------decimal 用于进行精确控制运算精度 有效位数 四舍五入等操作
#--------logging 提供了灵活记录事件 错误 警告
import schedule
def job():
    print('hahaha')

#schedule.every(3).seconds.do(job)
'''while True:
    schedule.run_pending()
    time.sleep(1)'''