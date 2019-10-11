Syns = {
    'main': 1, 'if': 2, 'then': 3,
    'while': 4, 'do': 5, 'static': 6,
    'int': 7, 'double': 8, 'struct': 9,
    'break': 10, 'else': 11, 'long': 12,
    'switch': 13, 'case': 14, 'typedef': 15,
    'char': 16, 'return': 17, 'const': 18,
    'float': 19, 'short': 20, 'continue': 21,
    'for': 22, 'void': 23, 'sizeof': 24,
    'ID': 25, 'NUM': 26, '+': 27, '-': 28,
    '*': 29, '/': 30, ':': 31,
    ':=': 32, '<': 33, '<>': 34,
    '<=': 35, '>': 36, '>=': 37,
    '=': 38, 'default': 39, 'do': 40,
    ';': 41, '(': 42, ')': 43, '#': 0,
    '%': 44, ',': 45, '.': 46, '?': 47,
    '==': 48
}

Iden = {
    'main', 'if', 'then', 'while', 'do', 'static',
    'int', 'double', 'struct', 'break', 'else', 'long',
    'switch', 'case', 'typedef', 'char', 'return', 'const',
    'float', 'short', 'continue', 'for', 'void', 'default',
    'sizeof', 'do'
}

Oper = {
    '+', '-', '*', '/', ':', ':=', '<', '<>', '<=', '>', '>=', '=', ';', '(', ')', '#', '%', ',', '.', '?', '=='
}

token = ''
summ = ''
oper = ''
syn = -1


def error(message):
    print(message)


def identifier(letter):
    global token
    global summ
    global syn
    global oper

    if oper:
        if oper in Oper:
            print('---    运算符和界符   ' + oper + ' : ' + str(Syns[oper]))
            oper = ''
        else:
            error('无效的操作符')
            oper = ''

    if summ:
        error(message='error:数字后加字母')
    else:
        token += letter


def number(letter):
    global token
    global summ
    global syn
    global oper

    if oper:
        if oper in Oper:
            print('---    运算符和界符   ' + oper + ' : ' + str(Syns[oper]))
            oper = ''
        else:
            error('无效的操作符')
            oper = ''

    if token:
        token += letter
    else:
        summ += letter


def other(letter):
    global token
    global summ
    global syn
    global oper

    if letter in Oper:
        if token:
            if token in Iden:
                print('---    关键字         ' + token + ' : ' + str(Syns[token]))
                token = ''
            else:
                print('---    其他标记ID     ' + token + ' : ' + str(Syns['ID']))
                token = ''
        elif summ:
            print('---    其他标记NUM    ' + summ + ' : ' + str(Syns['NUM']))
            summ = ''
        if oper + letter in Oper:
            oper += letter
        else:
            print('---    运算符和界符   ' + oper + ' : ' + str(Syns[oper]))
            oper = ''


def toprint():
    global token
    global summ
    global syn

    if token:
        if token in Iden:
            print('---    关键字         ' + token + ' : ' + str(Syns[token]))
            token = ''
        else:
            print('---    其他标记ID     ' + token + ' : ' + str(Syns['ID']))
            token = ''
    elif summ:
        print('---    其他标记NUM    ' + summ + ' : ' + str(Syns['NUM']))
        summ = ''


if __name__ == '__main__':
    fo = open("code.cpp")
    s = fo.read()
    for letter in s:
        if letter.isalpha():
            identifier(letter)
        elif letter.isdigit():
            number(letter)
        elif letter.isspace():
            toprint()
        else:
            other(letter)
    print('分析完毕')
