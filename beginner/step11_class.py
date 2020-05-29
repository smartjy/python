class fruit:
    color = 'red'
    def taste(self):
        return 'delicious'

apple = fruit()
print(apple.color)
print(apple.taste())

# class staff:
#     def salary(self):
#         return '10,000/hour'
# alba = staff()
# print(alba.salary())

class staff:
    bonus = 50000
    def salary(self):
        salary = 100000 + self.bonus
        return salary
alba = staff()
print('alba salay :', alba.salary())

class staff:
    def __init__(self, bonus):
        self.bonus = bonus
    def salay(self):
        salay = 100000 + self.bonus
        return salay
alba1 = staff(500000)
print ('alba1 salay :', alba1.salay())

alba2 = staff(600000)
print('alba2 salay :', alba2.salay())

