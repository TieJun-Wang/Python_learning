for item in range(3):
    pwd=int(input('请输入密码：'))
    if pwd==8888:
        print('密码输入正确')
        break
    else:
        print('密码不正确')
# while 语句
a=0
while a<3:
    pwd=int(input('请输入密码'))
    if pwd==8888:
        print('密码正确')
        break
    else:
        print("密码错误")
    a+=1