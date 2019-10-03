#非装饰器
import time
def f1():
    print('this is f1')

def f2():
    print('this is f2')

def print_time(func):
    print(time.time())
    func()

print_time(f1)
print_time(f2)