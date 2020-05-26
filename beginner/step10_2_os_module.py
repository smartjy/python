import os

# os.chdir('/Users/jyson/Developments/python/')

home_dir = os.environ.get('HOME')
print('Home Directory :', home_dir, '\n')

work_dir = os.getcwd()

file_path = os.path.join((work_dir), 'README.md')
print('File Path :', file_path)

test_dir = '/tmp/test.txt'

dir_name = os.path.dirname(test_dir)
base_name = os.path.basename(test_dir)
split_name = os.path.split(test_dir)
exists_file = os.path.exists(test_dir)
is_file = os.path.isfile(test_dir)
split_ext = os.path.splitext(test_dir)

print('Directory name :', dir_name)
print('Base name :', base_name)
print('Directory split :', split_name)
print('Exists File :', exists_file)
print('Is File :', is_file)
print('Split Ext :', split_ext)


