#枚举
from enum import Enum

class VIP(Enum):
    yellow=1
    green=2
    red=3
    black=4

print(VIP.green)
print(type(VIP.green))
print(VIP.green.name)
print(type(VIP.green.name))
print(VIP.green.value)
print(type(VIP.green.value))
print(VIP['green'])
print(type(VIP['green']))
for v in VIP:
    print(v)