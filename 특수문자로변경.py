##a[i] = '#' <-- 'str' object does not support item assignment
a = '파이썬완전재미있어요'
b = '##################'
for i in range(1,len(a),2):
    a = a.replace(a[i],'#')
print(a)