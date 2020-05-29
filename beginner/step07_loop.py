nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        # break
        continue
    print(num)

print ('')

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for i in range(1, 10):
#     print(i)

x = 0
while x < 10:
    print(x)
    x += 1

# for range
for count in range(3):
    print('for count', count, '\n')

text = 'apple'
for chara in text:
    print(chara)

brand_list = ['apple', 'samsung', 'lg']
for brand in brand_list:
    print('brand:', brand_list)