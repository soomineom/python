list1 = [0,0,0,0]
hap = 0

list1[0] = int(input('1번째 숫자:'))
list1[1] = int(input('2번째 숫자:'))
list1[2] = int(input('3번째 숫자:'))
list1[3] = int(input('4번째 숫자:'))

for i in range (0,4,1):
    hap = hap + list1[i]
##hap = list1[0] + list1[1] + list1[2] + list1[3]

print('합계: %d' %hap)
