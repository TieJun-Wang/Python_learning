#编码格式 
#UTF-8------Unicode的实现   
#文件读写原理 IO操作
# file=open("filename",'mode(w or r)','encoding')
file=open('a.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()
#文档打开的模式 r-只读 w-写 a-追加模式不存在则新建文本在开头存在则添加文本在末尾 b-以二进制打开文件不能单独使用 +-以读写方式打开也不能单独使用
file=open('b.txt','w',encoding='UTF-8')  #没有文档会自己创建文档 有文档输入文字会覆盖原文件
file.write('hello world 我喜欢学爬虫')
file.close()
file=open('b.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()
file=open('b.txt','a',encoding='UTF-8')
file.write('\n我喜欢你')
file.close()
file=open('b.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()
#图片的复制
src_file=open('logo.jpg','rb')
target_file=open('copylogo.jpg','wb')
target_file.write(src_file.read())
file.close()
#文件对象的常用方法 read(n) ----读取n个字符 readline()----列表显示每一行内容 writelines(str_list) 将字符串列表写进文本
file=open('c.txt','w+',encoding="UTF-8")
lst1=['你好\n','世界\n','Python\n']
file.writelines(lst1)
file.seek(0) #指针跳动到x位
print(file.readlines())
file.close() 
#tell() 返回当前指针所在位置 一个英文占一个字节 汉字三个字节 换行一个字节
#flush()-----把缓冲区内容写进文件但不关闭文件---即还可以继续进行操作
print('-_'*50)
#——————————————————————————with语句------上下文管理器
with open('c.txt','w+',encoding="UTF-8") as f_c:
    f_c.write('\n'.join(['你好',"我喜欢你","这个世界"]))
    print(f_c.tell())
    f_c.seek(0)
    print(f_c.read())
    print(f_c.tell())
    f_c.seek(0)
    print(f_c.readlines())

#————————————————————————————目录操作 os模块
import os  #-------os.system(xxx)  打开xxx
'''常见函数:getcwd()---返回当前目录          listdir(path)---返回指定路径下的文件和目录信息    
mkdir(path[,mode])---创建目录               makedirs(path1/path2...)---创建多级目录
rmdir(path)---删除目录                      removedirs(path1/path2...)---删除多级目录
chdir(path)---将path设置为当前工作目录'''
#os.system('calc.exe')
#os.startfile(r"C:\Users\王世宇\AppData\Local\Doubao\Application\Doubao.exe")  #-----直接调用可执行文件 加r就不用避免转义字符
print(os.getcwd())
lst00=os.listdir('../python')
print(lst00,os.getcwd())
#os.mkdir('a')
#os.makedirs('a/b/c')
#os.removedirs("a/b/c")
print(os.getcwd())
print(os.listdir())
os.chdir('C:\\Users\\王世宇\\Desktop')
print(os.getcwd())
#---------------os.path
'''abspath(path)---获取文件或者目录的绝对路径              exists(path)---用于判断文件目录是否存在
join(path,name)---将目录与目录或者文件名拼接起来            splitext()---分离文件名和扩展名
basename(path)---从一个目录中提取文件名                     dirname(path)---从一个路径中提取文件路径,不包括文件名
isdir(path)---判断是否为路径'''
import os.path
print(os.path)
print(os.getcwd())
os.chdir('C:\\Users\\王世宇\\Desktop\\python')
print(os.getcwd())
print(os.path.abspath('#list.py'))
print(os.path.exists('#list.py'))
print(os.path.join('C:\\Users\\王世宇\\Desktop\\python','demo11.py'))
print(os.path.split("C:\\Users\\王世宇\\Desktop\\python\\a.txt"))   #分离文件名
print(os.path.splitext('C:\\Users\\王世宇\\Desktop\\python\\a.txt'))  #分离文件名及其后缀
print(os.path.basename('C:\\Users\\王世宇\\Desktop\\python\\a.txt'))  #根据路径提取文件名
print(os.path.dirname('C:\\Users\\王世宇\\Desktop\\python\\a.txt'))
print(os.path.isdir('a.txt'))
# 案列练习————获取指定路径下的所有py文件
path1=os.getcwd()
lst_path=os.listdir(path1)
for file_py in lst_path:
    if file_py.endswith('.py'):
        print(file_py,end=" ")
print('-'*60)
# 案列练习————添加文件和walk应用
os.chdir(r'C:\Users\王世宇\Desktop\python\a\b')
with open('bbb.txt','w+',encoding='UTF-8') as fb:
    fb.write('您好世界')
os.chdir(r'C:\Users\王世宇\Desktop\python')
print(os.getcwd())
path2=os.getcwd()
lst_path2=os.walk(path2)
print(lst_path2)
for dirpath,dirname,filename in lst_path2:
    print(dirpath)
    print(dirname)
    print(filename)
    print("-"*50)

def find_real_path(filename,search_path):
    os.chdir(search_path)
    print(os.getcwd())
    print('_'*50)
    for dirpath,dirname,filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(dirpath,filename)
        return None
    
print(find_real_path('bbb.txt',r'C:\Users\王世宇\Desktop\python'))


