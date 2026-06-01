#Str
#字符串为不可变序列 可用 ' ', " ",''' ''' 来定义
#字符串的驻留机制
#交互情况的几种情况: 字符串的长度为0或1 符号标识符的字符串 字符串只在编译时进行驻留而非运行时 [-5,256]之间的整数数字
a="hello"
b='world'
print(' '.join([a,b]))  #拼接时使用join拼接效率更高  ------'x'.join()
#强制驻留 x=sys.intern(y)   #交互式中成立
#——————————字符串的查询操作的方法
#-------index()，find()  查找substr第一次出现的位置 index如查找不存在则输出 valuerror   rindex(),rfind() 查找最后一次出现的位置 
s1='hello,hello'
print(s1.index('lo'))
print(s1.rindex('lo'))
print(s1.find('lo'))
print(s1.rfind('lo'))
print(s1.find('k')) #----如无相对应的输出负一
#print(s1.index('k'))  #------如无对应的会报错
#——————————字符串的大小写转换 upper大写 lower小写  转换之后会产生新的字符串
st1='hello python'
a=st1.upper()
print(a,id(a),id(st1))
print(a,a.lower(),id(a))
st2='Hello World'
print(st2,st2.swapcase())  #------.swapcase()所有的大写变为小写 小写变为大写
print(st2.swapcase(),st2.capitalize())#or .title() 将开头转化为大写，其他均变成小写 
#——————————字符串的常用操作方法
st3='hello,Python'
print(st3.center(20,'*'))  #------居中对齐
print(st3.ljust(20,'*'))   #------左对齐
print(st3.rjust(20,'*'))   #------右对齐
print(st3.zfill(20))       #------右对齐用零填充
#——————————字符串的劈分
st4='hello world python'
print(st4)
print(st4.split())     #-----分割 默认为空格
st5='hello|world|python'
print(st5,st5.split(sep='|',maxsplit=2))  #----指定符号进行分割 maxsplit----最大劈分次数
print(st5,st5.rsplit(sep='|',maxsplit=1))  #-----从右边开始分割
#——————————字符串的判断方法
print('1.','hello'.isidentifier())   #判断是合法标识符吗
print('2.','\t'.isspace())           #判断是否全部由空白字符组成(回车，换行，水平制表符)
print('3.',"hello".isalpha())        #判断是否全部由字母组成
print('4.','123'.isdecimal())        #判断是否全部由十进制数字组成  
print('5','1241252152'.isnumeric())  #判断是否全部由数字组成
print('6.',"214aaabbb".isalnum())    #判断是否全部由字母和数字组成
#——————————字符串的替换replace与合并join
sss='hello,python，python，python'
print(sss.replace('python','Java',2)) #-----将xxx替换为yyy 如有重复xxx可以加最多次数
print('|'.join(sss))       #按序列形式(元组，字符串等等)分开
print("❤️".join('我喜欢你'))
sss1=['hello','world','python']
print(sss1,'%'.join(sss1))
#——————————字符串的比较  从左到右依次比较字母的源符
print('apple'>'app','apple'>'banana') 
print(ord('a'),ord('b'))
print(ord('杨'),ord('王'),'杨'>'王')
print(chr(92),chr(93),chr(93)>chr(92))
#——————————字符串的切片操作 x[start:end;step]
a1='hello,python'
print(a1.split(sep=','))
a2=a1[:5]
print(a2,id(a1),id(a2))
a3=a1[6:]
print(a3)
a4='!'
a5=a2+a4+a3
print(id(a5),a2+a4+a3,id(a2+a4+a3))  #-------改变字符串id全变 重新生成
print(a1[::-1])     #--------倒置
a6='我喜欢你'
print(a6[::-1])
#————————————格式化字符串  按一定格式输出的字符串  %s-字符串 %i或%d-整数 %f-浮点数
import math
name='张三'
age=20
height=168.5
print('我叫%s,今年%i岁,身高是%f'%(name,age,height))
#-------保留字符串的宽度表示(应用于保留小数点的位数)
print('我的名字是%10s'% 'elisa')
print('%.4f'% 3.1415926)  #-----保留四位小数 round(xx,num)
print('%10.4f'% 3.1415926)  #-----同时表示宽度和精度
print(type('%10.4f'% 3.1415926))
a='%10.4f'% 3.1415926
print(a,a.center(20,'|'))
#以花括号{}做占位符 '{索引}'.fomat(引用)
print('我的名字是{0},今年是{1}岁,身高是{2},我真的是{1}岁'.format(name,age,height))
print('{0:.3f} {1:10.3}'.format(math.e,3.1415926))   #----- :.xf保留x位小数  :m.x 宽度为m保留x位数 
#另一种表达------f'xxx{} '
print(f'我叫{name},我的年龄是{age}')
print(f'{math.e:.3f}')
#——————————字符串的编码转换
#--------编码 将字符串转换为二进制
ss='你好世界'
print(ss.encode(encoding='GBK')) #在UBK中 一个中文占两个字节
print(ss.encode(encoding='UTF-8')) #UTF-8中 一个中文占三个字节
#--------解码
#byte 代表一个二进制数据
byte=ss.encode(encoding='GBK')
print(byte.decode(encoding="GBK"))
#颜色的调用 m:样式结束符 0:恢复默认 1:加粗高亮 2:淡化 4:下划线 5:闪烁
''' 前景色 背景色 颜色
        30	40	黑色
        31	41	红色
        32	42	绿色
        33	43	黄色
        34	44	蓝色
        35	45	紫色
        36	46	青色
        37	47	白色'''
print('\033[0;4;35m颜色测试\033[0m')