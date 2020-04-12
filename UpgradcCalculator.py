class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def minus(self, val):
        self.value -= val

cal = Calculator()
cal.add(20)
cal.minus(10)
print(cal.value)

#객체 변수 value가 100이상의 값을 가질 수 없게
#Calculator클래스 상속받아서
class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, val):
        if self.value >= 100:
            self.value = 100

cal1 = MaxLimitCalculator()
cal1.add(60)
cal1.add(80)
print(cal1.value)