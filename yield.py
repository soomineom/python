# def genFunc():
#     yield 1
#     yield 2
#     yield 3
#
# print(list(genFunc()))

def genFunc(num):
    for i in range(0,num):
        ##0 ~ 4반복
        yield i
        print('제너레이터 진행 중')
for data in genFunc(5):
    ##num에 5대입
    print(data)