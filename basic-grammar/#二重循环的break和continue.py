#二重循环的break和continue
'''流程控制语句在二重循环的应用'''
for i in range(0,5):
    for j in range(1,11):
        if j%2==0:
           continue
        print(j,end=" ")
    print()
    