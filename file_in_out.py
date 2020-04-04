# inFp, outFp = None, None
# inStr = ""
#
# inFp = open('C:/Windows/notepad.exe', 'rb')
# outFp = open('C:/Temp/notepad.exe', 'wb')
#
# while True:
#     inStr = inFp.read(1)
#     if not inStr:
#         break
#
#     outFp.write(inStr)
#
# inFp.close()
# outFp.close()
# print('---복사완료---')

num1 = input('숫자1: ')
num2 = input('숫자2: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        result = num1/num2

except ValueError:
    print('문자열은 숫자로 변환 X')
except ZeroDivisionError:
    print('0으로 나누기 X')
except KeyboardInterrupt:
    print('ctrl+c 입력')
