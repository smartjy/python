# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = []
# for n in nums:
#     lst.append(n*n)

# lst = [ n for n in nums]

# lst = map(lambda n: n*n, nums)
#
# print(lst)



# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int, a))
# print(a)
# print(len(a))

# new_list = []
# for n in nums:
#     if n % 2 == 0:
#         new_list.append(n)
# print(new_list)
#
# my_lst = [ n for n in nums if n%2 ==0 ]
# print(my_lst)

# my_lst = []
# for letter in 'abcd':
#     for num in range(len(letter)):
#         my_lst.append((letter, num))
#
# print(my_lst)
# my_lst = [(letter, num) for letter in 'abcd' for number in range(4)]
# print(my_lst)

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#
# # print zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
#
# print(my_dict)

nums = [1,2,3,4,5,6,7,8,9]
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)

for i in my_gen:
    print(i)