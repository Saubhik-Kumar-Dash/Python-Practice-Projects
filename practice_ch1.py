"""
1.Write a program to print Twinkle twinkle little star poem in python.
2.Use REPL and print the table of 5 using it.
3.Install an external module and use it to perform an operation of your interest.
4.Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
5.Label the program written in problem 4 with comments
"""

#1 
#print("""Twinkle, twinkle, little star,
#How I wonder what you are!
#Up above the world so high,
#Like a diamond in the sky.

#When the blazing sun is gone,
#When he nothing shines upon,
#Then you show your little light,
#Twinkle, twinkle, all the night.

#Then the trav'ller in the dark,
#Thanks you for your tiny spark,
#He could not see which way to go,
#If you did not twinkle so.

#In the dark blue sky you keep,
#And often thro' my curtains peep,
#For you never shut your eye,
#Till the sun is in the sky.

#'Tis your bright and tiny spark,
#Lights the trav'ller in the dark:
#Tho' I know not what you are,
#Twinkle, twinkle, little star.""")

#2 We can use python as a calculator by typing “python” + ↵ on the terminal.This opens REPL or Read Evaluate Print Loop.

#3 pip install pyttsx3
"""import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Mortal, saala kutta")
engine.runAndWait()"""

#4 and #5
"""import os

# Get the path to the directory (you can replace '.' with any specific path)
directory_path = '/'

# List all files and directories in the given path
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
"""