import os

# os.chdir('/Users/jyson/Developments/python/')

home_dir = os.environ.get('HOME')
print('Home Directory :', home_dir, '\n')

work_dir = os.getcwd()

file_path = os.path.join((work_dir), 'README.md')
print('File Path :', file_path)

dir_name = os.path.dirname('/Users/jyson/Developments/python/beginner/README.md')
split_name = os.path.split('/Users/jyson/Developments/python/beginner/README.md')
print('Directory name :', dir_name)
print('Directory split :', dir_name)

# print(os.path.basename('/Users/jyson/Developments/python/beginner/README.md'))