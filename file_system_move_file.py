import os

source = 'main.txt'
dest = 'newfile.txt'

os.rename(source,dest)

print('the file has been renamed from {source} to {dest}')