# Set
nums = {1, 2, 3, 4, 5, 1, 2, 3}
print(nums)

java = {'John', 'Banner', 'Tony'}
python = set(['Tony', 'Steve', 'Banner'])

# Intersection
print('Intersection :', java & python)
print('Intersection :', java.intersection(python))

# Union
print('Union :', java | python)
print('Union :', java.union(python))

# Difference
print('Difference :', java - python)
print('Difference :', java.difference(python))

# Add
python.add('Thor')
print('Python Thor Add', python)

# Remove
python.remove('Tony')
print('Python Tony Remove', python)

# Type modify
hero = {'Thor', 'Hulk', 'Ironman'}
print('hero var type :', hero, type(hero))

hero = list(hero)
print('hero var type :', hero, type(hero))

hero = tuple(hero)
print('hero var type :', hero, type(hero))

hero = set(hero)
print('hero var type :', hero, type(hero))


