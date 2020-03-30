def plus(v1,v2):
    result = 0
    result = v1 + v2
    return result

def minus(v1,v2):
    result = 0
    if v1 > v2:
        result = v1 - v2
    elif v2> v1 :
        result = v2 - v1
    else:
        result = 0

    return result


def calc(v1,v2,op):
    result = 0
    if op == '+':
        plus(v1,v2)
    elif op == '-':
        minus(v1,v2)
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2

    return result

v1,v2,op = 0,0,''

op = input('계산입력(+, -, *, /) : ')
var1 = int(input('첫 번째 숫자 : '))
var2 = int(input('두 번째 숫자: '))

res = calc(var1,var2,op)

print('계산기: %d %s %d = %d ' %(var1, op, var2, res))