'''
aa = []
bb = []
i=0

for i in range(0,100):
    aa.append(i)
for i in range(0,100):
    bb.append(aa[99-i])

print('%d %d' %(bb[0],bb[99]))

'''

##강의6 pdf 67쪽 예제
aa = []
bb = []
i, num = 0, 0

for i in range(0,200):
    aa.append(num)
    num += 3
for i in range(0,200):
    bb.append(aa[199-i])

print('bb[0]에는 %d, bb[199]에는 %d' %(bb[0], bb[199]))



