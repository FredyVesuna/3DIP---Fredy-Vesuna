#ScienceQuiz_v8.py
#Multi-choice science quiz for primary to high-school students (ages 6-18) with 3 levels of difficulties
#Fredy Vesuna, 25/07/2023

#Imports the classes 
from tkinter import *
#Imports extra themed widgets
from tkinter import ttk
#Imports module to display messagebox
from tkinter import messagebox
#Imports random for the questions to come out in random order
import random

#defining the class
class ScienceQuiz:
    #Method constructor that is used when an object is created of the ScienceQuiz class
    def __init__(self, parent):
#-------------------------------------------------------#
        #List for the answer choices in the quiz
        self.options_buttons = []
        #Variable that will be used for where information about the user might be displayed
        self.informationframe = None
        #Variable for the section where the science quiz questions will be shown
        self.questionsframe = None
        #Variable for the section where the summary of the quiz will be displayed
        self.summaryframe = None
        
        #This will store the users name
        self.name_value = StringVar()
        #This will store the users age
        self.age_value = StringVar()
        #This will store the users gender
        self.gender_value = StringVar()
        #This will store the selected difficulty level of the quiz    
        self.difficulty_level = StringVar()

#-------------------------------------------------------#
        
#----------------------------------------------------------------- Configuring the Widgets for HomeFrame -------------------------------------------------------------#
        #Creating a frame called homeframe
        self.homeframe = Frame(parent)
        self.homeframe.grid(row = 0, column = 0)
        
        #Creating the heading label
        self.headinglabel = Label(self.homeframe, bg = "dodgerblue", fg = "black", width = 70, padx = 40, pady = 20, text = "WELCOME TO THE SCIENCE QUIZ 2023", font = ("Times New Roman", "16", "bold"))
        #Making the label span across 5 columns
        self.headinglabel.grid(columnspan = 5)
        
        #Creating a description label with the text being black and specific widths
        self.descriptionlabel = Label(self.homeframe, fg = "black", width = 35, padx = 300, pady = 10, text = """
                                      This is an academic quiz for a purpose to gain intellectual knowledge on science. The quiz will be multichoice with
                                      3 different difficulties (easy, medium and hard). My target users for the quiz are for any ages.
                                      This is because the quiz is appropriate for anyone to access and should be accessible to any age.
                                      The purpose of the science quiz to create an increase in popularity of science.
                                      This is for people who are interested in science and want to challenge their knowledge by completing
                                      a quiz or if who is new to science and want to test their knowledge after studing or learning the science topic.""", font = ("Times New Roman", "12"))
        self.descriptionlabel.grid (column = 0)
            
        #Creating a button called Participate and Enter Your Details that then calls the show_information_frame method
        self.submit = ttk.Button(self.homeframe, text="Participate and Enter Your Details!", command=self.show_information_frame)
        #Placing the button on the 11th row and 1st column of the homeframe
        self.submit.grid(row=11, column=1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #Defining method
    def show_information_frame(self):
#-------------------------------------------------------#
        # If there is a questionsframe
        if self.questionsframe:
            #Destory the questionsframe
            self.questionsframe.destroy()
            #If there is a informationframe
        if self.informationframe:
            #Destroy the informationframe
            self.informationframe.destroy()

        #Clearing the buttons list, meaning it will it will remove previous questions and move to next question
        self.options_buttons.clear()
        #Hiding homeframe
        if self.homeframe:
            self.homeframe.grid_forget()
#-------------------------------------------------------#

#--------------------------------------------------------- Configuring the Widgets for InformationFrame -------------------------------------------------------------#        
        #Creating an information frame for the quiz
        self.informationframe = Frame(root)
        #positioning the frame using grid method 
        self.informationframe.grid(row=0, column=0)

        #Adding a heading label invloving colour, width, text, size and font
        self.headinglabel = Label(self.informationframe, bg = "light green", fg = "black", width = 40, padx = 40, pady = 20, text = "ENTER YOUR INFORMATION", font = ("Times New Roman", "16", "bold"))
        #positioning the heading label 
        self.headinglabel.grid(columnspan = 5)
        
        #Asking the user to enter their first name 
        self.namelabel = Label(self.informationframe, text = " Enter your first name:", width = 60, font = ("Calibri", "11", "bold"))
        #positioning the label
        self.namelabel.grid(row = 2, column = 0, sticky = N)

        #Creating a input box for the users name
        self.name = StringVar()
        self.name.set("")
        #The text box for the user to enter their name with ttk/
        self.nameentry = ttk.Entry(self.informationframe, textvariable = self.name_value, width = 25)
        #positioning the widget
        self.nameentry.grid(row = 3, column = 0, sticky = N)

        #Asking the user to enter their age
        self.agelabel = Label(self.informationframe, text = "Enter your age:", width = 21, font = ("Calibri", "11", "bold"))
        #Positioning the label 
        self.agelabel.grid(row = 4, column = 0, sticky = N,)

        #Creating a input box for the users age
        self.age = StringVar()
        #setting the value to an empty string so it resets the users previous value
        self.age.set("")
        #Input box being placed in the information frame
        self.ageentry = ttk.Entry(self.informationframe, width = 25, textvariable = self.age_value)
        #Positioning the widget
        self.ageentry.grid(row = 5, column = 0, sticky = N)

        #Asking the user to entet their gender
        self.genderlabel = Label(self.informationframe, text = "Enter your gender:", width = 24, font = ("Calibri", "11", "bold"))
        #Positioning the label
        self.genderlabel.grid(row = 6, column = 0, sticky = N)

        #Creating the drop down list for the selection of gender
        select_gender = ["Male", "Female", "Other"]

        #Using Combobox to allow the user to select an option from the list
        self.gender = ttk. Combobox (self.informationframe, values = select_gender, width = 22, state = "readonly", textvariable=self.gender_value)
        #Positioning the widget          
        self.gender.grid(row = 7, column = 0, sticky = N)

        #Assking the user to select a quiz difficulty
        self.difficultylabel = Label(self.informationframe, text = "Which difficulty would you like to choose:", width = 55, padx = 60, pady = 10, font = ("Times New Roman", "16", "bold underline"))
        #Positioning the label for quiz difficulty
        self.difficultylabel.grid(row = 12, column = 0, sticky = N)

        #Creating radio buttons for selecting the quiz difficulty
        self.difficulty = ["Easy Quiz", "Medium Quiz", "Hard Quiz"]
        #This will store the selected difficulty level
        self.difficulty_level = StringVar()
        #Setting the default difficulty level to 0 which is the Easy Quiz
        self.difficulty_level.set(0)
        #Creating an empty list to store the difficulty level radio buttons
        self.difficulty_buttons = []

         
        
        for i in range (len(self.difficulty)):
            #Creating a radio button for the information frame 
            button = ttk.Radiobutton(self.informationframe, variable = self.difficulty_level, value = i, text = self.difficulty[i], width = "40")
            self.difficulty_buttons.append(button)
            #Placed in the vertical position of i+14 and first column and North side
            button.grid(row = i+14, column = 0, sticky = N)

        #Creating a button called Proceed to the Questions! to go the show_questions_frame method
        self.submit = ttk.Button(self.informationframe, text="Proceed to the Questions!", command= self.show_questions_frame)
        #Positioning the button on the 20th row
        self.submit.grid(row=20, column=0)

        #Creating a button called Back to Home and adding to the informationframe. When the button is clicked it will go back to the show_home_frame
        self.back_to_home_button = ttk.Button(self.informationframe, text="Back to Home", command=self.show_home_frame)
        #Positioning the button on the 21st row
        self.back_to_home_button.grid(row=21, column=0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        
#-------------------------------------------------------- Configuring Method to Check User's Information -------------------------------------------------------------#
    def validate_input(self):
        #Recieving the user values for name, age and gender
        name = self.name_value.get().strip()
        age = self.age_value.get().strip()
        gender = self.gender_value.get()

        #This checks if the name is invalid, meaning if the name is left empty
        if not name:
            messagebox.showerror("Input Error", "Error: Please enter a valid name.")
            return False

        #This checks if there there only letters. If there is a different character it will cause the error message box to appear 
        if not name.isalpha():
            messagebox.showerror("Input Error", "Error: Name can only contain letters.")
            return False

        #Checks if the age is emptpy
        if not age:
            messagebox.showerror("Input Error", "Error: Please enter your age.")
            return False

        #Checks if the age is valid
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Error: Please enter a valid age.")
            return False
        #Checking if the age is within the suitable range
        if age < 6 or age > 18:
            messagebox.showerror("Input Error", "Error: You are too young or too old to particpate.")
            quit()

        #Checking if the user has selected a gender
        if not gender:
            messagebox.showerror("Inputer Error", "Error: Please select your gender.")
            return False
        
        #Means the quiz will proceed when it passes all the checks 
        return True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------- Configuring Method to Show Questions Frame ------------------------------------------------------#
    #
    def show_questions_frame(self):
        #Checking if the users input is valid
        if not self.validate_input():
            return

        if self.informationframe:
            #Destroying the informationframe 
            self.informationframe.destroy()
        if self.questionsframe:
            self.questionsframe.destroy()

        #Hiding the homeframe
        if self.homeframe:
            self.homeframe.grid_forget()


        #Creating a questionsframe for the quiz questions
        self.questionsframe = Frame(root, padx=20, pady =20)
        #Variable that keep track of the question index 
        self.index = 0
        #Variable that keep track of the question score
        self.score = 0
        #Positioning the questionsframe
        self.questionsframe.grid(row=0, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------- Configuring the Widgets for QuestionFrame ----------------------------------------------------#
        #Creating a label for questionsframe called SCIENCE QUIZ QUESTIONS 
        self.headinglabel = Label(self.questionsframe, bg = "lightgrey", fg = "green", width = 50, padx = 40, pady = 20, text = "SCIENCE QUIZ QUESTIONS", font = ("Times New Roman", "16", "bold"))
        #Positioning the heading label
        self.headinglabel.grid(row = 0, columnspan = 3)
        
#--------------------------------------------------------------------------------------------------------------------
        #The selected difficulty are selected as integers (0 for easy, 1 for medium, 2 for hard)
        selected_difficulty = int(self.difficulty_level.get())

        #Question banks for questions for different difficulty levels
        question_banks = [
           
            [#Easy questions
                #Dictionaries invloving a list including indivual questions
                {
                    #Showing the text of the question
                    "question": "What is the chemical symbol for water?",
                    #List of options for the user to choose from
                    "options": ["H20", "CO2", "NaC1", "02"],
                    #Showing the correct answer
                    "correct_answer": "H20"
                },

                {
                    #Showing the text of the question
                    "question": "What is the name of the table where you can find all the chemcial elements?",
                    #List of options for the user to choose from
                    "options": ["Element Table", "Periodic Table", "Science Table", "Chemical Table"],
                    #Showing the correct answer
                    "correct_answer": "Periodic Table"
                },

                {
                    #Showing the text of the question
                    "question": "What does DNA stand for?",
                    #List of options for the user to choose from
                    "options": ["Digestion nitrogen acid", "Deoxyribonucleic acid", "Distribution negative acid", "Distribution negative arragment"],
                    #Showing the correct answer
                    "correct_answer": "Deoxyribonucleic acid"
                },

                {
                    #Showing the text of the question
                    "question": "What are the 3 states for matter?",
                    #List of options for the user to choose from
                    "options": ["Salt, Lice, Gas", "Side, Liquid, Gas", "Solid, Liquid, Green", "Solid, Liquid, Gas"],
                    #Showing the correct answer
                    "correct_answer": "Solid, Liquid, Gas"
                },

                {
                    #Showing the text of the question
                    "question": "What is the chemcial symbol for hydrogen?",
                    #List of options for the user to choose from
                    "options": ["H", "Na", "C", "He"],
                    #Showing the correct answer
                    "correct_answer": "H"
                },

                {
                    #Showing the text of the question
                    "question": "C is the symbol for which chemical element?",
                    #List of options for the user to choose from
                    "options": ["Chlorine", "Calcium", "Carbon", "Helium"],
                    #Showing the correct answer
                    "correct_answer": "Carbon"
                },

                {
                    #Showing the text of the question
                    "question": "What part of the body helps you move?",
                    #List of options for the user to choose from
                    "options": ["Eyes", "Muscles", "Lungs", "Pancreas"],
                    #Showing the correct answer
                    "correct_answer": "Muscles"
                },

                {
                    #Showing the text of the question
                    "question": "What star shines in the day and provides light?",
                    #List of options for the user to choose from
                    "options": ["Sun", "Mars", "Venus", "Moon"],
                    #Showing the correct answer
                    "correct_answer": "Sun"
                },

                {
                    #Showing the text of the question
                    "question": "What is the young one of a cow called?",
                    #List of options for the user to choose from
                    "options": ["Puppy", "Kitten", "Calf", "Baby"],
                    #Showing the correct answer
                    "correct_answer": "Calf"
                },

                {
                    #Showing the text of the question
                    "question": "Which is the largest land animal?",
                    #List of options for the user to choose from
                    "options": ["Lion", "Tiger", "Elephant", "Rhinoceros"],
                    #Showing the correct answer
                    "correct_answer": "Elephant"
                },
                    
            ],
        #--------------------------------------------------------------------------------------------

            [ #Medium questions-------------------------------------------------------------------------------------------------------------------
                {
                    
                    #Showing the text of the question
                    "question": "What is the largest planet in our solar system?",
                    #List of options for the user to choose from
                    "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                    #Showing the correct answer
                    "correct_answer": "Jupiter"
                },

                {
                    #Showing the text of the question
                    "question": "Who invented the telephone?",
                    #List of options for the user to choose from
                    "options": ["Alexander Graham Bell", "Albert Einstein", "Charles Darwin", "Rosalind Franklin"],
                    #Showing the correct answer
                    "correct_answer": "Alexander Graham Bell"
                },

                {
                    #Showing the text of the question
                    "question": "Which is not a form of carbon?",
                    #List of options for the user to choose from
                    "options": ["Diamond", "Graphite", "Amorphous Carbon", "Ferrite"],
                    #Showing the correct answer
                    "correct_answer": "Ferrite"
                },

                {
                    #Showing the text of the question
                    "question": "What is the lightest elemet in the periodic table?",
                    #List of options for the user to choose from
                    "options": ["Helium", "Hydrogen", "Carbon", "Nitrogen"],
                    #Showing the correct answer
                    "correct_answer": "Hydrogen"
                },

                {
                    #Showing the text of the question
                    "question": "What energy emerges from motion?",
                    #List of options for the user to choose from
                    "options": ["Potential Energy", "Electrical Energy", "Kinetic Energy", "Consistent Energy"],
                    #Showing the correct answer
                    "correct_answer": "Kinetic Energy"
                },

                {
                    #Showing the text of the question
                    "question": "What is Earth's only natural satellite?",
                    #List of options for the user to choose from
                    "options": ["Sun", "Moon", "Venus", "Mars"],
                    #Showing the correct answer
                    "correct_answer": "Moon"
                },

                {
                    #Showing the text of the question
                    "question": "Which nutrient plays an essential role in muscle building?",
                    #List of options for the user to choose from
                    "options": ["Protein", "Carbohydrates", "Fat", "Iron"],
                    #Showing the correct answer
                    "correct_answer": "Protein"
                },

                {
                    #Showing the text of the question
                    "question": "Plants need which gas to perform photosynthesis?",
                    #List of options for the user to choose from
                    "options": ["Hydrogen", "Carbon Monoxide", "Carbon Dioxide", "Oxygen"],
                    #Showing the correct answer
                    "correct_answer": "Carbon Dioxide"
                },

                {
                    #Showing the text of the question
                    "question": "Which scientist proposed the three laws of motion?",
                    #List of options for the user to choose from
                    "options": ["Isaac Newton", "Thomas Alva Edison", "Albert Einstein", "Stephen Hawking"],
                    #Showing the correct answer
                    "correct_answer": "Isaac Newton"
                },

                {
                    #Showing the text of the question
                    "question": "What part of the plant conducts photosynthesis?",
                    #List of options for the user to choose from
                    "options": ["Branch", "Leaf", "Root", "Trunk"],
                    #Showing the correct answer
                    "correct_answer": "Leaf"
                },
                    
            ],
            #--------------------------------------------------------------------------------------------------------------
            
            [#Hard questions-------------------------------------------------------------------------------------------------
                {
                    #Showing the text of the question
                    "question": "Who proposed the theory of general relativity?",
                    #List of options for the user to choose from
                    "options": ["Albert Einstein", "Isaac Newotn", "Stephen Hawking", "Galileo Galilei"],
                    #Showing the correct answer
                    "correct_answer": "Albert Einstein"
                },

                {
                    #Showing the text of the question
                    "question": "What is the smallest planet in our solar system?",
                    #List of options for the user to choose from
                    "options": ["Saturn", "Venus", "Mercury", "Neptune"],
                    #Showing the correct answer
                    "correct_answer": "Mercury"
                },

                {
                    #Showing the text of the question
                    "question": "What is the chemical symbol for table salt?",
                    #List of options for the user to choose from
                    "options": ["S", "NaCl", "NH4F", "H2O"],
                    #Showing the correct answer
                    "correct_answer":"NaCl"
                },

                {
                    #Showing the text of the question
                    "question": "What is the normal pH level of human blood?",
                    #List of options for the user to choose from
                    "options": ["7.40", "5", "6.40", "2.3"],
                    #Showing the correct answer
                    "correct_answer":"7.40"
                },

                {
                    #Showing the text of the question
                    "question": "Which of the following planet was first discovered by the telescope?",
                    #List of options for the user to choose from
                    "options": ["Uranus", "Venus", "Jupitar", "Saturn"],
                    #Showing the correct answer
                    "correct_answer":"Uranus"
                },

                {
                    #Showing the text of the question
                    "question": "Which material of the following has the highest transparency?",
                    #List of options for the user to choose from
                    "options": ["Paper", "Wood", "Metal", "Glass"],
                    #Showing the correct answer
                    "correct_answer": "Glass"
                },

                {
                    #Showing the text of the question
                    "question": "Which organ covers the entire body and protects it?",
                    #List of options for the user to choose from
                    "options": ["Skin", "Heart", "Brain", "Lung"],
                    #Showing the correct answer
                    "correct_answer": "Skin"
                },

                {

                    #Showing the text of the question
                    "question": "How long does it take for light to travel from the sun to the Earth?",
                    #List of options for the user to choose from
                    "options": ["4 mintues and 23 seconds", "7 minutes and 4 seconds", "10 minutes and 55 seconds", "8 minutes and 19 seconds"],
                    #Showing the correct answer
                    "correct_answer": "8 minutes and 19 seconds"
                },

                {
                    #Showing the text of the question
                    "question": "How many elements are listed on the periodic table?",
                    #List of options for the user to choose from
                    "options": ["100", "88", "118", "140"],
                    #Showing the correct answer
                    "correct_answer": "118"
                },

                {
                    #Showing the text of the question
                    "question": "Who won the physics Nobel Prize in 1921?",
                    #List of options for the user to choose from
                    "options": ["Albert Einstein", "Marie Curie", "Charles Darwin", "Stephen Hawking"],
                    #Showing the correct answer
                    "correct_answer": "Albert Einstein"
                },
  
                    














             
            #--------------------------------------------------------------------------------------------------------------
            ]
        ]

        #Selecting 10 random question from the question_banks
        self.selected_questions = random.sample(question_banks[selected_difficulty], 10)

        #List to store the questions
        self.questions = [q["question"] for q in self.selected_questions]
        #List to store the correct answers
        self.correct_answers =[q["correct_answer"] for q in self.selected_questions]

        #Creating a variable to store the current question number
        self.current_question_var = IntVar()
        #Setting the current question value to 1
        self.current_question_var.set(1)

        #Creating labels to display the questions 
        self.question_label = Label(self.questionsframe, text=self.questions[0], font=("Times New Roman", 12), wraplength = 400, justify = "center") 
        #Positioning the label
        self.question_label.grid (row=1, column=0, columnspan=3, padx=10, pady=10)

        #Variable to store the user's selected answer
        self.options_var = StringVar()
        #Setting this variable to none meaning it will reset the chosen answer for the next question from the previous question
        self.options_var.set(None)
        #Puts the questions in order and can give the numbers to questions
        for i, option in enumerate(self.selected_questions[0]["options"]):
            #Creating radio buttons for the answers in the questionsframe
            rb = Radiobutton(self.questionsframe, text=option, variable=self.options_var, value=option, font=("Times New Roman",10))
            #Positioning the radio button and placed at a vertical position of i+2
            #It is being positioned in the Left side (W)
            rb.grid(row=i+2, column=1, columnspan=1, padx=10, pady=5, sticky=W)
            self.options_buttons.append(rb)

#----------------------------------------------------------------------------------------------------------------------------
        #Creating a button called submit to proceed to the next question
        self.submit_button = ttk.Button(self.questionsframe, text = "Submit", command=self.check_answer)
        #Positioning the submit button
        self.submit_button.grid(row=7, column =0, columnspan=3, pady=10)

        #Creating a label for the questionsframe to display the feedback for the user
        self.feedback_label= Label(self.questionsframe, text = "", font=("Times New Roman", 12), wraplength=600, justify="center")
        #Positioning the feedback label
        self.feedback_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        #Creating a Back to Information button which will call the show_information_frame when clicked
        self.back_to_information_button = ttk.Button(self.questionsframe, text="Back to Information", command=self.show_information_frame)
        #Positioning the buttonq
        self.back_to_information_button.grid(row=8, column=1)

        #Creating a Back to home button which will call the show_home_frame when clicked
        self.back_to_home_button = ttk.Button(self.questionsframe, text="Back to Home", command=self.show_home_frame)
        self.back_to_home_button.grid(row=9, column=1)
#-----------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------- Configuring Method to the Check User's Answers -----------------------------------------------------------#
    def check_answer(self):
        #Capturing the users answer for the question
        user_answer = self.options_var.get()
        #Converting the current_question_index to a 0 based index
        current_question_index = self.current_question_var.get() - 1

        #If the user has selected an answer
        if user_answer:
            #Getting the correct answer from the list of the correct answer
            correct_answer = self.correct_answers[current_question_index]

            #Comparing the users answers to the correct answers to see if it is correct or incorrect
            if user_answer == correct_answer:
                self.score += 1

            #Giving a review to the user whether it is correct or incorrect
            self.feedback_label.config(text=f"Your answer is {'correct!' if user_answer == correct_answer else 'incorrect!'}")
            #Positioning the label 
            self.feedback_label.grid(row = 8, column = 2)
            # Move to the next question
            self.current_question_var.set(current_question_index + 2)  

    
            #Checking whether all the answers had been answered
            if current_question_index == len(self.questions) - 1:
                #Showing the summary frame
                self.show_summary_frame()
            #Otherwise it will show the next question
            else:
                self.show_next_question()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------- Configuring Method for User to Move on to Next Question ----------------------------------------------------#
    def show_next_question(self):
        #Converting the current_question_index to a 0 based index
        current_question_index = self.current_question_var.get() - 1
        #Changing the question label with the text of the next question
        self.question_label.config(text=self.questions[current_question_index])

        #Destroy the old radio buttons for the restart
        for rb in self.options_buttons:
            rb.destroy()

        #Clearing the list of the old radio buttons
        self.options_buttons.clear()


        #Creating a new radio button for the answers options of the next question and add them to the GUI
        for i, option in enumerate(self.selected_questions[current_question_index]["options"]):
            #Creating the radio button for the questionsframe
            rb = Radiobutton(self.questionsframe, text=option, variable=self.options_var, value=option, font=("Times New Roman", 10))
            #Positioning the radio buitton
            rb.grid(row=i + 2, column=1, columnspan=1, padx=10, pady=5, sticky=W)
            self.options_buttons.append(rb)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------- Configuring Widgets for the SummaryFrame ----------------------------------------------------------------#
    def show_summary_frame(self):
        #Destroying the questionsframe
        if self.questionsframe:
            self.questionsframe.destroy()

        #Destroying the summaryframe
        if self.summaryframe:
            self.summaryframe.destroy()

        #Creating a new frame for the summary page
        self.summaryframe = Frame(root, padx=20, pady=20)
        self.summaryframe.grid(row=0, column=0)

        #Creating labels for the summary page including Name, Age, Gender, Score
        summary_page = ["Name", "Age", "Gender", "Score"]
        self.summaryframe_labels = []

        for i in range(len(summary_page)):
            heading = Label(self.summaryframe, text=summary_page[i], anchor=W, width=15, bg="lightblue", font=("Arial", 14, "bold"))
            self.summaryframe_labels.append(heading)
            heading.grid(row=1, column=i, sticky="EW")

        #Displaying the summary frame labels sepreatly for Name, Age, Gender and Score
        self.summary_name = Label(self.summaryframe, text=self.name_value.get(), bg="lightblue")
        #Positioning the labels
        self.summary_name.grid(row=3, column=0, sticky="EW")

        self.summary_age = Label(self.summaryframe, text=self.age_value.get(), bg="lightblue")
        self.summary_age.grid(row=3, column=1, sticky="EW")

        self.summary_gender = Label(self.summaryframe, text=self.gender_value.get(), bg="lightblue")
        self.summary_gender.grid(row=3, column=2, sticky="EW")

        self.summary_score = Label(self.summaryframe, text=str(self.score) + "/10", bg="lightblue")
        self.summary_score.grid(row=3, column=3, sticky="EW")

        #Creating a button to restart the quiz
        self.restart_button = ttk.Button(self.summaryframe, text="Restart Quiz", command=self.restart_quiz)
        #Postioning the restart button
        self.restart_button.grid(row=4, column=1, padx=5, pady=10)

        #Creating a button to quit the quiz
        self.quit_button = ttk.Button(self.summaryframe, text="Quit", command=self.quit_quiz)
        #Postioning the quit button
        self.quit_button.grid(row=4, column=2, padx=5, pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------- Configuring Method to allow User to Go Back -------------------------------------------------------------#
    def show_home_frame(self):
        #Destroying the questionsframe
        if self.questionsframe:
            self.questionsframe.destroy()
        #Destroying the informationframe
        if self.informationframe:
            self.informationframe.destroy()
        #Show the home frame at row 0 and column 0 
        if self.homeframe:
            self.homeframe.grid(row=0, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------- Configuring Methods to allow User to Restart or Quit the Quiz ----------------------------------------------#

    def restart_quiz(self):
        #Destory the summaryframe
        if self.summaryframe:
            self.summaryframe.destroy()

        # Reset all variables
        self.name_value.set("")
        self.age_value.set("")
        self.gender_value.set("")
        self.difficulty_level.set(0)

        # Reset radio button selection
        self.difficulty_level.set(None)
        
        # Destroy questionsframe
        if self.questionsframe:
            self.questionsframe.destroy()
        #Destory informationframe
        if self.informationframe:
            self.informationframe.destroy()

        # Go back to the homeframe
        self.show_home_frame()

    #Quitting the application
    def quit_quiz(self):
        root.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            

#Main routine - This will run the script as the main module and the name of the parent window (root)
#__name__ is a variable defined for each script
if __name__ == "__main__":
    #Main application window
    root = Tk()
    #This is the title of my GUI quiz
    root.title("Science Quiz 2023")
    GUI = ScienceQuiz(root)
    #Starting the application
    root.mainloop()
    
