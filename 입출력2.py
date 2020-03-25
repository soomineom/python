
ss = input('입력 문자열==> ')
pp = ''

for i in range(0,len(ss)):
    pp = ss.replace('o','$')
print('출력 문자열==> %s' %pp)
