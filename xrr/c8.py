#JSON
import json

a = '{"name":"xrr","age":20}'

b = json.loads(a)
print(type(b))
print(b)
print(b['name'])
print(b['age'])
c = json.dumps(b)
print(type(c))
print(c)
