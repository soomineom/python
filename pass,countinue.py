# for i in (1,2,3):
#     if i:
#         print('pass %d '%i)
#         pass
#     print('mjsjinsu pass')
#
# for i in (4,5,6):
#     if i:
#         print('pass %d' %i)
#         continue
#     print('mjsjinsu continue')


##강의 44p
#
def para(v1,v2,v3 = 0):
    result = 0
    result = v1+v2+v3
    return result

hap = 0

hap = para(10,20)
print('매개변수 2개인 함수호출결과 >>> %d' %hap)
hap = para(10,20,30)
print('매개변수 3개인 함수호출결과 >>> %d' %hap)


##강의 46p

def para (*para) :
    result = 0
    for num in para:
        result = result + num

    return result

hap = 0

hap = para(10,20)
print('%d'%hap)
hap = para(10,20,30)
print('%d'%hap)

##47p
def dic(**para):
    for k in para.keys():
        print('%s -> %d명' %(k,para[k]))

dic(트와이스 = 9, 소녀시대 = 7, 블랙핑크 = 4)