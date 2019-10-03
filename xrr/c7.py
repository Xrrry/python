#search/findall
import re
a='life is short,i use python'

r=re.search('life(.*)python',a)
print(r.group(1))
s=re.findall('life(.*)python',a)
print(s)