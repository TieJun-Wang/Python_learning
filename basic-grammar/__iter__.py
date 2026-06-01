#迭代器 __iter__ and __next__的应用
#书写一个倒计时
import time
#面向对象法书写 迭代器
class Countdown:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<0:
            raise StopIteration
        num=self.current
        self.current-=1
        return num
for i in Countdown(3):
    print(f'倒计时:{i:2d}s',end="\r",flush=True)
    time.sleep(1)
#用列表进行书写
for i in range(3,-1,-1):
    print(f'倒计时:{i:2d}s',end='\r',flush=True)
    time.sleep(1)
# yield 语句 使用 yield的函数称为生成器generator
def countdown(n):
    while n>0:
        yield n
        n-=1
generator=countdown(5)
print(f"\n\b{next(generator):1d}")
print(next(generator))
for i in generator:
    print(i)

#yield语句写斐波那契数列
def fibonacci(n):   #输出n位的数列
    a,b,counter=0,1,1
    while True:
        if counter>n:
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)
for i in f:
    print(i,end=" ")
