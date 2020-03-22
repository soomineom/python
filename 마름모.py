i = 0

while i < 9:
    if i < 5:
        k = 0

        '''
        i=0, k=4보다 작을 때
        i=1, k=3보다 작을 때
        '''
        while k < 4 - i :
            print(' ', end = '') ##공백 출력
            k += 1

        k = 0

        while k < i * 2 + 1:
            print('\u2605', end='')
            k += 1


    else:
        k = 0
        while k < i -4 :
            print('', end='')
            k += 1
        k = 0

        
