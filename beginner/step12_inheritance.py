class animalBaseClass:
    animallegs = 4
    def walk(self):
        print('walk')
    def cry(self):
        print('cry cry')
    def getLegsNum(self):
        print(self.animallegs)

class dogClass(animalBaseClass):
    def __init__(self):
        print('This is the dog')

baduk = dogClass()
print(baduk.walk())
print(baduk.cry())
print(baduk.getLegsNum())