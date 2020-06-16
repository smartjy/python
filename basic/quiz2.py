class House:
    def __init__(self, localtion, house_type, deal_type, price, completion_year):
        self.location = localtion
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House('gangnam', 'apt', 'sale', '10,000', '2010')
house2 = House('mapo', 'opt', 'rental', '5,000', '2007')
house3 = House('songpa', 'bpt', 'rental', '5,000', '2010')

houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    house.show_detail()

print('Total {} Houses'.format(len(houses)))