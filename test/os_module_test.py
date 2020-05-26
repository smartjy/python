#!/usr/local/bin/python3

import os
from datetime import datetime

#print('Current Work Directory :',  os.getcwd(), '\n')

#print('Current Work Directory File List :', os.listdir(), '\n')

# Make
#os.makedirs('test_dir/sub_dir')
os.mkdir('create_dir')

#os.removedirs('test_dir/sub_dir')
#os.rmdir('test_dir')

#os.rename('rename_file.txt', 'rename_file1.txt')

#print('File stats :', os.stat('rename_file1.txt'))
#print('File stats mtime :', os.stat('rename_file1.txt').st_mtime)

mod_time = os.stat('rename_file1.txt').st_mtime

print('File state timestamp :', datetime.fromtimestamp(mod_time))

# modify st_mtime timestamp
#mod_time = os.stat('rename_file1.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))

home_dir = os.environ.get('HOME')
print('Home Directory :', home_dir, '\n')




