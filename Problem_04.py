'''
4. Write a python program to print the contents of a directory using the os module. Search
online for the function which does that

'''

import os

path = "."  # Current directory

contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)

