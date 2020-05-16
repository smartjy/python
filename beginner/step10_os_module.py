import os

print(dir(os), '\n')

# os.chdir('/Users/jyson/Developments/python')

print('OS get Current Work Directory :', '\n',  os.getcwd(), '\n')
print('Current Work Directory File List :', '\n', os.listdir(), '\n')

# Make
# os.makedirs('os_module_makedirs')
# os.mkdir('os_module_makedirs/sub_dir1')

# Remove
# os.removedirs('os_module_makedirs')
# os.rmdir('os_module_makedirs')
# os.rmdir('os_module_makedirs/sub_dir1')

# Rename
# os.rename('os_rename_file.txt', 'os_rename_file1.txt')

# Stats
print('os_rename_file1 stats :', '\n', os.stat('os_rename_file1.txt'))
print('os_rename_file1 size :', '\n', os.stat('os_rename_file1.txt').st_size)
