Syns = {
    'main': 1, 'if': 2, 'then': 3,
    'while': 4, 'do': 5, 'static': 6,
    'int': 7, 'double': 8, 'struct': 9,
    'break': 10, 'else': 11, 'long': 12,
    'switch': 13, 'case': 20, 'typedef': 15,
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
    '==': 48, '++':49,'--':50,'+=':51,'-=':52,'!=':53,
    '[':54, ']':55,'\\?':56,'{':57,'}':58
}

Iden = {
    'main', 'if', 'then', 'while', 'do', 'static',
    'int', 'double', 'struct', 'break', 'else', 'long',
    'switch', 'case', 'typedef', 'char', 'return', 'const',
    'float', 'short', 'continue', 'for', 'void', 'default',
    'sizeof', 'do'
}

Oper = {
    '+', '-', '*', '/', ':', ':=', '<', '<>', '<=', '>', '>=', '=', ';', '(', ')', '#', '%', ',', '.', '?', '==','++','--','+=','-=','!=','[',']','{','}'
}

token = ''
summ = ''
oper = ''
syn = -1
inspe = False
waitfor = False
inmuti = False
hasone = False


def error(message):
    print(message)


def identifier(letter):
    global token
    global summ
    global syn
    global oper

    if oper:
        if oper in Oper:
            print('<'+str(Syns[oper])+'>    '+'---    运算符或界符   ' + oper)
            oper = ''
        else:
            error('无效的操作符')
            oper = ''

    if summ:
        error(message='error:数字后加字母')
        summ = ''
    else:
        token += letter


def number(letter):
    global token
    global summ
    global syn
    global oper

    if oper:
        if oper in Oper:
            print('<'+str(Syns[oper])+'>    '+'---    运算符或界符   ' + oper)
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
    global inspe
    global waitfor
    global inmuti

    if letter in Oper:
        if token:
            if token in Iden:
                print('<'+str(Syns[token])+'>    '+'---    关键字         ' + token)
                token = ''
            else:
                print('<'+str(Syns['ID'])+'>    '+'---    其他标记-ID    ' + token)
                token = ''
        elif summ:
            print('<'+str(Syns['NUM'])+'>    '+'---    其他标记-NUM   ' + bin(int(summ)).replace('0b',''))
            summ = ''
        if oper + letter in Oper:
            oper += letter
        elif oper + letter == '//':
            inspe = True
        elif oper + letter == '/*':
            inmuti = True
        else:
            print('<'+str(Syns[oper])+'>    '+'---    运算符或界符   ' + oper)
            oper = ''+letter
    elif letter == '\\':
        toprint()
        waitfor = True


def toprint():
    global token
    global summ
    global syn

    if token:
        if token in Iden:
            print('<'+str(Syns[token])+'>    '+'---    关键字         ' + token)
            token = ''
        else:
            print('<'+str(Syns['ID'])+'>    '+'---    其他标记-ID    ' + token)
            token = ''
    elif summ:
        print('<'+str(Syns['NUM'])+'>    '+'---    其他标记-NUM   ' + bin(int(summ)).replace('0b',''))
        summ = ''


if __name__ == '__main__':
    fo = open("code.cpp")
    s = fo.read()
    for letter in s:
        if inmuti == False:
            if inspe==False:
                if waitfor==False:
                    if letter.isalpha():
                        identifier(letter)
                    elif letter.isdigit():
                        number(letter)
                    elif letter.isspace():
                        toprint()
                    else:
                        other(letter)
                else:
                    print('<56>    ---    其他标记-ID    \\' + letter)
                    waitfor = False
            else:
                if letter == '\n':
                    oper = ''
                    inspe = False
        else:
            if hasone and letter=='/':
                hasone = False
                inmuti = False
            elif letter == '*':
                oper = ''
                hasone = True
    print('分析完毕')
    fo.close()

