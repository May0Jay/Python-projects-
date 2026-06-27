'''
2. Write a program to fill in a letter template given below with name and date.
(letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# ''')

# Creating an variable to store the name and date given by user 
name = input("Enter your name: ")
date = input("Enter date: ")

# using an f"" string we are creating an format to print the latter exect as given above 
print(f'''
Dear {name},
you are selected
{date}
      ''')

# ------------------------------------------------------------------x--------------------------------------------------------------------------------------
