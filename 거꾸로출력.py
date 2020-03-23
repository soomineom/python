sen = input('문자열을 입력하세요: ')
printsen=''

for i in range(len(sen)):
    printsen = printsen + sen[len(sen)-(i+1)]
print('거꾸로 출력하기 --> %s' %printsen)