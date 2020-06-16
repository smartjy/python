# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

customers = ['John', 'Son', 'Kim', 'Lee']
for cus in customers:
    print('Hello!! {} '.format(cus))


lst = [1, 3, 5]
for i in range(1, 11):
    if i in lst:
        continue
    print('i = {}'.format(i))


nums = [1,2,3,4,5]
nums = [i+100 for i in nums]
print(nums)

name = ['Thor', 'Captain', 'Ironman', 'Wanda']
name = [len(i) for i in name]
print(name)
