##강의3 19p 동전교환
money = int(input('교환할 돈은 얼마?: '))

coin500 = money // 500 ##500으로 나눈 몫
money = money % 500 ## 500으로 나누고 나머지

coin100 = money // 100
money = money % 100

coin50 = money // 50
money = money % 50

coin10 = money //10
money = money % 10

print('500원짜리 ==> %d개' %coin500)
print('100원짜리 ==> %d개' %coin100)
print('50원짜리 ==> %d개' %coin50)
print('10원짜리 ==> %d개' %coin10)
print('바꾸지 못한 잔돈 ==> %d' %money)

