'''
5. Label the program written in problem 4 with comments.

'''
# we are importing an module using import function 
import os

# creating an variable and stroing an path 
path = "."  # Current directory

# now creating an another variable and storing am function on it 
contents = os.listdir(path)

# now we are taking an out put in it 
print("Contents of the directory:")
for item in contents:
    print(item)

# ----------------------------------------------------------x--------------------------------------------------------------------
