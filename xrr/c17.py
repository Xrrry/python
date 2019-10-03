#装饰器/语法糖
import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(name1):
    print('this is f1')
    print(name1)

@decorator
def f2(name1,name2):
    print('this is f2')
    print(name1 + '\n' +name2)
   
f1('123')
f2('123','232')