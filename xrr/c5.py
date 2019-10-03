#正则表达式
import re

a='c|c++4|j3a343va|46python|3434c#|ja12vas4cr6i76pt'
# print(a.index('python')>-1)
# print('pythoo' in{ a)
r=re.findall('[a-z]{3,6}',a)
print(r)
