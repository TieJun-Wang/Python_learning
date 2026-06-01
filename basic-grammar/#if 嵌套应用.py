#购物返现  会员密码8888
#购物返现 会员返现更多
print("-----欢迎来到返现查询系统-----")
a=int(input('请问你是否是会员(如是填1如不是填0)'))
b=0
if a==1:
    print('尊敬的会员您好')
    while b<3:
        psw=int(input('请输入您的会员密码'))
        if psw==8888:
            print('密码正确,尊敬的会员您好')
            break
        else:
            b+=1
            if b==3:
                print('密码输入失败次数过多,请稍后再试')
                break
            print("抱歉您输入的密码有误请重新输入,剩余次数为",3-b)
elif a==0:
    print('尊敬的用户您好')
else:
   print('请输入正确的数字')
   b+=3
#print('尊敬的会员您好' if a==1 else '尊敬的用户您好')
if a==0 or 3-b!=0:
    money=float(input('请输入您的月度消费金额'))
    if a==1:
        if money>=500 and money<=1000:
           print("您的返现金额是",money*0.15)
        elif money>1000 and money<=2000:
           print('您的返现金额是',money*0.2)
        elif money>2000:
           print('您的返现金额是',money*0.25)
        else:print("抱歉，您的月度消费金额不够返现门槛")
    else:
        if money>=500 and money<=1000:
          print('您的返现金额是',money*0.1)
        elif money>1000 and money<=2000:
          print('您的返现金额是',money*0.15)
        elif money>2000:
          print('您的返现金额是',money*0.2)
        else:print("抱歉，您的月度消费金额不够返现门槛")  
if a==0 or 3-b!=0:
   print('感谢您的查询')