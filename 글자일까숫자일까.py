ss = input('문자열 입력: ')

for i in range(len(ss)):
    if (ss.isdigit() == True):
        print('숫자입니다')
        break
    elif (ss.isalpha() == True):
        print('글자입니다')
        break
    elif (ss.isalpha() == True or ss.isdigit() == True):
        print('글자+숫자입니다')
        break
    else:
        print('모르겠습니다.')
        break