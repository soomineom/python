class Fruit:
    name = ""
    weight = 0

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight

fruit1 = Fruit('Apple', 2)
fruit2 = Fruit('Banana', 3)

print('과일1 >> 이름:%s, 무게: %d kg' %(fruit1.getName(), fruit1.getWeight()))
print('과일2 >> 이름:%s, 무게: %d kg' %(fruit2.getName(), fruit2.getWeight()))