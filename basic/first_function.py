def profile(name, age, *language):
# def profile(name, age):
    print('Name: {}, Age: {}'.format(name, age), end=' ')
    for lang in language:
        print(lang, end=' ')
    print()

profile('Tony', 23, 'JAVA', 'C', 'GO', 'Python')