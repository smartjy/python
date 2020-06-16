class laptop:
    def __init__(self, pc_seq, brand, name, size):
        self.pc_seq = pc_seq
        self.brand = brand
        self.name = name
        self.size = size
        print('[{}] PC Information: {}, {}, {}'.format(self.pc_seq, self.brand, self.name, self.size))

mypc = laptop('1', 'Apple', 'Macbook', '13')
mypc = laptop('2', 'Samsung', 'Note9', '15')
mypc = laptop('3', 'LG', 'Gram', '14')

# pc_seq = 1
# brand1 = 'Apple'
# name1 = 'Macbook'
# size1 = '13'
#
# print('[{}] PC Information: {}, {}, {}'.format(pc_sec, brand1, name1, size1))
#
# pc_seq = pc_seq + 1
# brand2 = 'Samsung'
# name2 = 'Note9'
# size2 = '15'
#
# print('[{}] PC Information: {}, {}, {}'.format(pc_sec, brand2, name2, size2))