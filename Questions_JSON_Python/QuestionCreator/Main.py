#Purpose: Have a Simple Program that allows for creating and updating JSON data.
#   This is the main file where the program will run to prompt for questions
import json
import os
from Questions_Handler import *

# - - - - - VARIABLES - - - - - 

choice = ""     #Determines what the user wants to do
appOn = True    #Bool to Determine whether the program is on or off

question = ""   #What is the question. Meant to be used in a loop
answer = ""     #The answer to ^. Meant to be used in a loop

FILE_LOCATION = "C:\\Users\\1211d\\Desktop\\Computer Science\\Personal Projects\\C#\\Minecraft Quiz Game\\Questions_JSON_Python\\"

# - - - - - PROGRAM STARTS HERE - - - - - 

#   Program Loop
while appOn:
    qh = question_handler() #Creating the QH object
    #Prompting Question
    print("What would you like to do?\nCreate a Database (CD) | Update a Database (UD) | Finished (OFF): ") 
    choice = str(input().upper())
    
    #Checking Choice
    if choice == "CD":      #Create Database
        #Naming JSON file
        name = ""
        name = str(input("Name of your file: "))
        qh.create_database(name.lower(), FILE_LOCATION) #Creates the Database

    elif choice == "UD":    #Update Database
        print("You chose to UPDATE a database!")

    elif choice == "OFF":   #Turning App Off
        print("App will be turned off!")
        appOn = False

    else:                   #Invalid Choice
        print("You did not choose a valid option") 


