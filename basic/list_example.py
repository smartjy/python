languge = ['Java', 'Go', 'Python', 'Bash']
print('languge :', languge)

print(languge.index('Python'))

# Add
print('\n##### ADD #####')
languge.append('TypeScript')
print('languge append:', languge)

languge.insert(1, 'Java Script')
print('languge insert:', languge)

# Remove
print('\n##### REMOVE #####')
print('languge pop target:', languge.pop())
print('languge latest:', languge)
print('languge count(Java):', languge.count('Java'))

# Sort
print('\n##### SORT #####')
nums = [1, 3, 5, 2, 4]
nums_sort = nums.sort()

print('nums sort()  :', nums.sort())
# print(n.sort())
print('nums sorted():', sorted(nums))
print('nums sorted() reverse:', sorted(nums, reverse=True))
print('nums clear:', nums.clear())