##암호화, 해독 프로그램

inFp, ouFp = None,None
inStr,outStr = "", ""
inList, outList = [], []
i , num = 0, 0

sel = input('1.암호화 // 2.암호 해석 중 선택 : ')
inFname = input('입력 파일명 입력: ')
outFname = input('출력 파일명 입력: ')

if sel == 1:
    num = 100
elif sel == 2:
    num = -100

inFp = open(inFname, 'r', encoding='utf-8')
ouFp = open(outFname, 'w', encoding='utf-8')

while True:
    inStr = inFp.readline()
    if not inStr: #0이면 not 붙이면 true 되니까~
        break #string아니면 멈추기

    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum += num
        ch2 = chr(chNum)
        outStr = outStr + ch2

    ouFp.write(outStr)

ouFp.close()
inFp.close()

print('{} --> {} 변환 완료' .format(inFname, outFname))






