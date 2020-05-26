
def find_all_hobbyists(hobby, hobbies):
    return [set(hobbies)]

hobbies = {
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

print(find_all_hobbyists('Yoga', hobbies));