import os

inFp = None
fNname, inList, inStr = "", [], ""

fNname = input('파일명 입력: ')

if os.path.exists(fNname):
    inFp = open(fNname, "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")

    inFp.close()
else:
    print('%s <--- 파일 없음. ' %fNname)