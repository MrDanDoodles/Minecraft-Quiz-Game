#Purpose: This program handles everything dealing with data:
#   Creating JSON files, loading and uploading them, and appending data
import json

class question_handler():

    # - - - - - CONSTRUCTOR - - - - - 

    def __init__(self):
        #VARIABLES
        self.question_dictionary = { }   #Dict to contain all questions and answers
    #END constructor

    # - - - - - FUNCTIONS - - - - - 

    #   Function for creating database
    def create_database(self, name_of_file, file_location):
        #Prompting User to create first question
        question = str(input("Lets start off with an intitial question: ")) #Receiving Question
        answer = str(input("Answer to ^: "))      #Receiving Answer

        #Appending Q&A to Dict
        self.question_dictionary[question] = answer  #Appending the Q&A

        #Printing as text
        print(self.question_dictionary)
        print("Amount of questions: " + str(len(self.question_dictionary)))

        #Creating the JSON file
        with open(f"{file_location}{name_of_file}.json" , "w") as json_file:
            json.dump(self.question_dictionary, json_file, indent=4)

        #Assuring User that File was created
        print(f"{name_of_file}.json was created!")

    #END create_database




