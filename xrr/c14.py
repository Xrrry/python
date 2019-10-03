#reduce
from functools import reduce

list_x = [1,2,3,4,5,2,2,4,21]

f = reduce(lambda x,y:x*y,list_x)

print(f)