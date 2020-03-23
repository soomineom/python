ss = input('날짜(연/월/일) 입력 ==> ')
bb = ''

bb = ss.split('/')
print('입력한 날짜의 10년 후 ==> ' + str((int(bb[0])+10)) + '년' , end='')
print(bb[1] + '월', end='')
print(bb[2] + '일')