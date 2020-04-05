# def selfCall():
#     print('하', end='')
#     selfCall()
# selfCall()

# def count(num):
#     if num >= 1:
#         print(num, end=' ')
#         count(num-1)
#     else:
#         return
#
# count(10)
# count(20)


##팩토리얼 연산은 외워두기!!
def factorial(num):
    if num<= 1:
        return num
    else:
        return num * factorial(num - 1)
        ##1보다 크면 자기 자신 곱하기 나머지~

print(factorial(4))
print(factorial(10))