#闭包
origin = 0

def factory(pos):
    def go(step):
        nonlocal pos
        now=pos+step
        pos=now
        return pos
    return go

tourist = factory(origin)
print(tourist(3))
print(tourist(4))
print(tourist(3))