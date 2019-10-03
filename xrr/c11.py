#非闭包
origin = 0

def go(step):
    global origin
    now = origin + step
    origin = now
    return origin

print(go(2))
print(go(4))
print(go(5))