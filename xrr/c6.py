#正则表达式
import re
a = 'AVD8768234376453DWAW967DFD33'


def convert(value):
    matched = value.group()
    if int(matched) > 5:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, a)
print(r)
