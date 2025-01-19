#Purpose: This program handles everything dealing with data:
#   Creating JSON files, loading and uploading them, and appending data
import json
from msilib.schema import File

class question_handler():

    # - - - - - CONSTRUCTOR - - - - - 

    def __init__(self, file_location):
        #VARIABLES
        self.question_dictionary = { }      #Dict to contain all questions and answers
        self.FILE_LOCATION = file_location  #The file location where the databases are
    #END constructor

    # - - - - - FUNCTIONS - - - - - 

    #   Function for CREATING database
    def create_database(self, name_of_file):
        #Prompting User to create first question
        question = str(input("Lets start off with an intitial question: ")) #Receiving Question
        answer = str(input("Answer to ^: "))      #Receiving Answer

        #Appending Q&A to Dict
        self.question_dictionary[question] = answer  #Appending the Q&A

        #Printing as text
        print(self.question_dictionary)
        print("Amount of questions: " + str(len(self.question_dictionary)))

        #Creating the JSON file
        with open(f"{self.FILE_LOCATION}{name_of_file}.json" , "w") as json_file:
            json.dump(self.question_dictionary, json_file, indent=4)

        #Assuring User that File was created
        print(f"{name_of_file}.json was created!")

    #END create_database

    #   Function for UPDATING databasees
    def update_database(self, name_of_file):
        #Local Variables
        loopOn = True
        
        #Getting data from JSON file
        with open(f"{self.FILE_LOCATION}{name_of_file}.json", "r") as json_file:
            data = json.load(json_file) #Assinging json data to a var named data
        print(f"The {name_of_file}.json was located and ready for use!")

        #Checking the amount of questions there are
        print("Question Count: " + str(len(data)))

        #Append Question Loop
        while loopOn:
            #Getting Q&A
            question_name = str(input("Question: "))
            answer = str(input("Answer to ^: "))
            
            #Assigning Q&A to data
            data[question_name] = answer

            #Checking to see if user wants to add another question:
            choice = str(input("Add another question?: Y or N: ").upper())
            if choice == "N":
                print(data)
                print(f"Attempting to update {name_of_file}.json")
                loopOn = False
            else:
                print("Please Continue")
        
        #updating json
        with open(f"{self.FILE_LOCATION}{name_of_file}.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Update was successful")
    #END update_database


        




