
##강의7 29p
a = input('입력 문자열 ==>')
b = ''

if (a.startswith('(') == False):
    a = '(' + a
if (a.endswith(')') == False):
    a = a + ')'
print('출력 문자열 ==>%s' %a)