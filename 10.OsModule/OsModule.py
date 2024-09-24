# Basic opening writing and reading files in python
f = open('example.txt','w+')
f.write('Writing something in file')
f.close() #Remember closing a file is important as it could cause unexpected errors if left open.

#USING OS.WALK
import os
x = os.getcwd()
filepath = f'{x}\\Example_Top_Level'
for dirpath, dirnames, filenames in os.walk(filepath):
    print(f'Currently looking at {dirpath} \n')
    print(f'Subfolder are: ')
    for directory in dirnames:
        print(f'\t subfolders are {directory} \n')
    print(f'Files are: ')
    for file in filenames:
        print(f'\t files are {file} \n')
