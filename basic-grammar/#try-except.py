#try-except
try:
    n1=int(input('请输入一个整数:'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
    print('结果为:',result)
except ZeroDivisionError:
    print('对不起,除数不能为零')
except ValueError:
    print('请输入数字而非文字')
except BaseException as e:
    print(e)

#————————————try...except...else...finally结构
try:    
    na=int(input('请输入一个整数:'))
    nb=int(input('请输入另一个整数:'))
    resulta=na/nb
except BaseException as e:
    print('出错了，请输入正确的值')
    print('错误类型为:',e)
else:
    print('计算结果为',resulta)
finally:                            #无论是否报错都会执行
    print('感谢您的使用')


#————————————————————————常见的异常类型——————————————————————————#
#ZeroDivisionError         被零除的异常
#IndexError   索引引用异常  如引用的索引超过范围
#KeyError     键取用异常    如取用字典没有的键dict.['none']
#NameError    未声明错误
#SyntaxError  语法错误
#ValueError   传入无效的参数 如将字符串int

#——————————Traceback模块
import traceback
try:
    print('-----------')
    print(1/0)
except:
    traceback.print_exc()