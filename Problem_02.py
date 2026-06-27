'''
2. Write a python program to find remainder when a number is divided by z.

'''

# we are creating an variables and storing an input function that takes the number from user 
x = int(input("Enter your number: "))          # Enter  the number that breakes (divides) the number z
z = int(input("Enter your number: "))          # Enter the number that gives the reminder 

# now we are going to use the maths here
reminder = z % x 

# this prints gives the reminder here 
print("the reminder of the z is: ", reminder)

# here we are importing an module named "Pyttsx3" that can speak 
import pyttsx3

# we have to feed what we have to speak 
say = pyttsx3.speak(f"your reminder is {reminder}")
print (say)         # output is an voice recoard 

# -------------------------------------------------------------------x--------------------------------------------------------------------------------
