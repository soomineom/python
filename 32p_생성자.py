# class Car:
#     color = ""
#     speed = 0
#
#     def __init__(self):
#         self.color = "red"
#         self.speed = 0
#         print('init 실행')
#
#     def upSpeed(self,value):
#         self.speed += value
#     def downSpeed(self,value):
#         self.speed -= value
#
# myCar1 = Car()
# myCar1.upSpeed(100)
# myCar2 = Car()
#
# print(myCar1.color)
# print(myCar1.speed)


##매개변수있는 생성자
class Car:
    color = ""
    speed = 0

    def __init__(self,value1,value2):
        self.color = value1
        self.speed = value2

myCar1 = Car('red', 100)
myCar2 = Car('blue', 70)

print('자동차1의 색: %s, 속도 %d km' %(myCar1.color, myCar1.speed))
print('자동차2의 색: %s, 속도 %d km' %(myCar2.color, myCar2.speed))
