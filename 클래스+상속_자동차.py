class Car:
    def __init__(self):
        self.speed = 0

    def upSpeed(self,value):
        self.speed += value
        print('현재속도(Super Class): %d' %self.speed)

    def downSpeed(self,value):
        self.speed -= value
        print('현재속도(Super Class): %d' %self.speed)

class Sedan(Car): #Car상속받음
    def upSpeed(self,value):
        self.speed += value

        if self.speed >= 150:
            self.speed = 150

        print('현재속도(Sub Class): %d' %self.speed)

class Sonata(Sedan):
    pass
#48p 클래스 상속

class Truck(Car):
    pass
    # def upSpeed(self,value):
    #     self.speed += value
    #
    #     print('현재속도(Sub Class): %d' % self.speed)

class Suv(Car):
    def upSpeed(self,value):
        self.speed += value

        if self.speed >= 150:
            self.speed = 150

    def downSpeed(self,value):
        self.speed -= value
        print('현재속도(Sub Class): %d' %self.speed)

truck1 = Truck()
sedan1 = Sedan()
suv1 = Suv()
sonata1 = Sonata()

print('트럭 -->', end="")
truck1.upSpeed(100)
#Car라는 슈퍼클래스의 upSpeed()메서드 호출

print('승용차 -->', end="")
sedan1.upSpeed(40)
#Sedan 인스턴스의 upSpeed()메서드 호출하면 14행에서 재정의된 upSpeed()메서드 호출

print('SUV -->', end="")
suv1.upSpeed(120)
suv1.downSpeed(80)

print('소나타 -->', end="")
sonata1.upSpeed(90)
