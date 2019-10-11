fo = open("code.cpp")
s = fo.read()
for line in s:
    if line=='\n':
        print('aaa')
    elif line==' ':
        print('bbb')
    else:
        print(line)

fo.close()
