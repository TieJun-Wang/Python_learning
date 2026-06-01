# continue函数
#输出1到50之间的所有5的倍数
for item in range(1,51):
    if item%5==0:
        print(item)
#使用continue函数
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
