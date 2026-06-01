#正则表达式 regular expression
import re
#例子
#1[3-9]\d{9}:第一位为数字1 第二位在3到9之间然后出现9次
'''------------------------------------re.match  -----从字符串的开头开始匹配(返回match对象否则返回none)
result = re.match('表达式',对象)  
#获取匹配项的值 result.group()
#获取匹配项索引 result.span()  开始索引start() 结束索引end()

------------------------------------re.search -----从字符串的任意位置开始,搜索第一个匹配项(返回match对象)
result = re.search('表达式',对象)
#获取匹配项的值 result.group()
#获取匹配项索引 result.span()  开始索引start() 结束索引end()

------------------------------------re.findall -----从任意位置开始,搜索所有匹配项(返回list)
result = re.findall('表达式',对象) 返回的是列表(list)

------------------------------------------re语法------------------------------------------
普通字符:字母、数字、汉字及大多数字符，直接匹配自身         .:匹配任意一个字符(除了\n)
\d:匹配数字 0-9                                         \D:匹配非数字
\w:匹配单词字符,a-z,A-Z,0-9,_,其他语言字符                \W:匹配非单词字符
[aeiou]:匹配其中的任何单个字符                            [^aeiou]:求反,匹配不在字符列表中的任何单个字符
[0-5]:表示范围                                           *:出现任意次(0或者无限次)
+:至少出现1次(1次或者无限次)                              ?:至多出现一次(0次或1次)
{m}:出现m次                                             {m,}:至少出现m次
{m,n}:出现m到n次                                         |:或的意思,匹配左右任意一个表达式
():分组,将括号里的多个字符视为一个单元  记得加索引          ^:匹配字符串开头
$:匹配字符串结尾                                         \s:匹配空格制表符换行符    
'''

s1='''用户ID: U12345, 邮箱: test_user@example.com, 手机号: 13812345678, 注册时间: 2025-05-07, 状态: 已激活(√)
    备用信息: 昵称: 豆包_AI, 旧手机号: 13900001111, 备用邮箱: backup@test.cn
    错误格式: 邮箱: bad-email, 手机号: 123456, 无效ID: X_999@, 乱码: 1a2b3c!@#$%^&*()'''
print(s1)
#匹配字符串中所有纯数字单个字符
print(re.findall(r'\d',s1))
#匹配所有连续数字串
print(re.findall(r'\d{2}',s1))
#匹配所有11位合法手机号
print(re.findall(r'1[3-9]\d{9}',s1))
#匹配U开头+5位数字用户ID
print(re.findall(r'U\d{5}',s1))
#匹配所有邮箱地址
print(re.findall(r'\w+@\w+\.\w+',s1,re.ASCII))
#匹配任意一个英文字母、数字、下划线
print(re.findall(r'\w',s1))
#匹配任意一个不是单词字符
print(re.findall(r'\W',s1))
#匹配开头第一行的用户ID
print(re.findall(r'用户ID:\s*(\w+)',s1))
#匹配状态参数
print(re.findall(r'状态:\s*(.*)',s1))

text = '''
姓名: 张三, 年龄: 20, 电话: 13678901234
邮箱: zhangsan@qq.com, 学号: S20250618
地址: 广州市天河路A123号, 邮编: 510000
备用邮箱: zs123@163.com
'''

#提取姓名后面的名字
print(re.findall(r'姓名:\s*(\w+)',text))
#提取年龄后面的数字
print(re.findall(r'年龄:\s*(\w+)',text))
#提取所有手机号
print(re.findall(r'电话:\s*(\d{11})',text))
#提取所有邮箱
print(re.findall(r'[\w.-]+@[\w.-]+\.[\w.]+',text))
#提取学号S开头+8位数字
print(re.findall(r'S\d{8}',text))
#提取六位数字邮编
print(re.findall(r'邮编:\s*(\d{6})',text))
#提取地址后面整串内容
print(re.findall(r'地址:\s*(\w+)',text))
#匹配所有邮箱:并取出后面邮箱
print(re.findall(r'邮箱:\s*(\w+@\w+\.\w+)',text))
#匹配以S开头的编号
print(re.findall(r'S\w+',text))
#提取所有纯数字串
print(re.findall(r'\d+',text))






