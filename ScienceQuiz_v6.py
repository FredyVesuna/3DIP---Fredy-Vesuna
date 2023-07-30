#ScienceQuiz_v1.py
#Science quiz for all ages with 3 levels of difficulties
#Fredy Vesuna, 22/07/2023

#This is the standard python interface tk GUI
from tkinter import *

from tkinter import ttk
#This module provides access to the Tk themed widget set. This gives a better look and feel to make the GUI asethetically pleasing for the user 

from tkinter import messagebox

#This will generate the questions in a random order
import random


#Defining science quiz GUI
class ScienceQuiz:

#__init__ is known as a constructor in object oriented programming. It is a concept to initalize the attributes of a class (sciencequiz)
#"self" is a variable that must be the prefix to all variables that will belong to the instances of the class
    def __init__(self, parent):
        self.options_buttons = []

#----------------------------------------------------------------- Widgets for Home Frame ---------------------------------------------------------------------------
        self.homeframe = Frame(parent)
        self.homeframe.grid(row = 0, column = 0)

        self.headinglabel = Label(self.homeframe, bg = "dodgerblue", fg = "black", width = 70, padx = 40, pady = 20, text = "WELCOME TO THE SCIENCE QUIZ 2023", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(columnspan = 5)

        self.descriptionlabel = Label(self.homeframe, fg = "black", width = 35, padx = 300, pady = 10, text = """
                                      This is an academic quiz for a purpose to gain intellectual knowledge on science. The quiz will be multichoice with
                                      3 different difficulties (easy, medium and hard). My target users for the quiz are for any ages.
                                      This is because the quiz is appropriate for anyone to access and should be accessible to any age.
                                      The purpose of the science quiz to create an increase in popularity of science.
                                      This is for people who are interested in science and want to challenge their knowledge by completing
                                      a quiz or if who is new to science and want to test their knowledge after studing or learning the science topic.""", font = ("Times New Roman", "12"))
        self.descriptionlabel.grid (column = 0)

        self.submit = ttk.Button(self.homeframe, text="Participate and Enter Your Details!", command=self.show_information_frame)
        self.submit.grid(row=11, column=1)



#----------------------------------------------------------------- Widgets for Information Frame ---------------------------------------------------------------------------

    def show_information_frame(self):
        self.homeframe.destroy()
        self.informationframe = Frame(root)
        self.informationframe.grid(row=0, column=0)

        self.headinglabel = Label(self.informationframe, bg = "light green", fg = "black", width = 40, padx = 40, pady = 20, text = "ENTER YOUR INFORMATION", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(columnspan = 5)


        self.namelabel = Label(self.informationframe, text = " Enter your first name:", width = 60, font = ("Calibri", "11", "bold"))
        self.namelabel.grid(row = 2, column = 0, sticky = N)

        self.name = StringVar()
        self.name.set("")
        self.nameentry = ttk.Entry(self.informationframe, textvariable = self.name, width = 25)#The text box for the user to enter their name with ttk/
        self.nameentry.grid(row = 3, column = 0, sticky = N)


        self.agelabel = Label(self.informationframe, text = "Enter your age:", width = 21, font = ("Calibri", "11", "bold"))
        self.agelabel.grid(row = 4, column = 0, sticky = N,)

        self.age = StringVar()
        self.age.set("")
        self.ageentry = ttk.Entry(self.informationframe, width = 25, textvariable = self.age)
        self.ageentry.grid(row = 5, column = 0, sticky = N)


        self.genderlabel = Label(self.informationframe, text = "Enter your gender:", width = 24, font = ("Calibri", "11", "bold"))
        self.genderlabel.grid(row = 6, column = 0, sticky = N)


        select_gender = ["Male", "Female", "Other"]

        self.gender = ttk. Combobox (self.informationframe, values = select_gender, width = 22)
        self.gender.grid(row = 7, column = 0, sticky = N)

        self.difficultylabel = Label(self.informationframe, text = "Which difficulty would you like to choose:", width = 55, padx = 60, pady = 10, font = ("Times New Roman", "16", "bold underline"))
        self.difficultylabel.grid(row = 12, column = 0, sticky = N)

        self.difficulty = ["Easy Quiz", "Medium Quiz", "Hard Quiz"]
        self.difficulty_level = StringVar()
        self.difficulty_level.set(0)
        self.difficulty_buttons = []

         #For loop
        for i in range (len(self.difficulty)):
            button = ttk.Radiobutton(self.informationframe, variable = self.difficulty_level, value = i, text = self.difficulty[i], width = "40")
            self.difficulty_buttons.append(button)
            button.grid(row = i+14, column = 0, sticky = N)
        
        self.submit = ttk.Button(self.informationframe, text="Proceed to the Questions!", command= self.showquestionsframe)
        self.submit.grid(row=20, column=0)


#------------------------------------------------------- Error Checking for User's Name and Age ------------------------------------------------------------------------


    def validate_input(self):
        name = self.name.get().strip()
        age = self.age.get().strip()
        gender = self.gender.get()

    # Checking if the user has entered a name
        if not name:
            messagebox.showerror("Input Error", "Error: Please enter a valid name.")
            return False

    # Checking if the name contains only letters
        if not name.isalpha():
            messagebox.showerror("Input Error", "Error: Name can only contain letters.")
            return False

    # Checking if the user has entered an age
        if not age:
            messagebox.showerror("Input Error", "Error: Please enter your age.")
            return False

    # Checking if the age is a valid integer
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Error: Please enter a valid age.")
            return False

        
    #Checking if the user has selected a gender
        if not gender:
            messagebox.showerror("Inputer Error", "Error: Please select your gender.")
            return False

        return True


#----------------------------------------------------------------- Widgets for Questions Frame ---------------------------------------------------------------------------

   
    def showquestionsframe(self):
        #Validate the input before showing the user the science quiz questions
        if not self.validate_input():
            return
        
        self.informationframe.destroy()
        self.questionsframe = Frame(root, padx=20, pady =20)
        self.index = 0
        self.score = 0
        self.questionsframe.grid(row=0, column=0)

        self.headinglabel = Label(self.questionsframe, bg = "lightgrey", fg = "green", width = 50, padx = 40, pady = 20, text = "SCIENCE QUIZ QUESTIONS", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(row = 0, columnspan = 3)

        #Difficulty level selected by the user (0 for easy , 1 for medium, 3 for hard
        selected_difficulty = int(self.difficulty_level.get())

        #Load question banks for each difficulty level
        question_banks = [
            #Easy Questions
            [
                {
                    "question": "What is the chemical symbol for water?",
                    "options": ["H20", "CO2", "NaC1", "02"],
                    "correct_answer": "H20"
                },
                

                {
                    "question": "What is the name of the table where you can find all the chemcial elements?",
                    "options": ["Element Table", "Periodic Table", "Science Table", "Chemical Table"],
                    "correct_answer": "Periodic Table"
                },

                {
                    "question": "What does DNA stand for?",
                    "options": ["Digestion nitrogen acid", "Deoxyribonucleic acid", "Distribution negative acid", "Distribution negative arragment"],
                    "correct_answer": "Deoxyribonucleic acid"
                },

                {
                    "question": "What are the 3 states for matter?",
                    "options": ["Salt, Lice, Gas", "Side, Liquid, Gas", "Solid, Liquid, Green", "Solid, Liquid, Gas"],
                    "correct_answer": "Solid, Liquid, Gas"
                },

                {
                    "question": "What is the chemcial symbol for hydrogen?",
                    "options": ["H", "Na", "C", "He"],
                    "correct_answer": "H"
                },
                    
                    
                    
            ],
            #Medium Questions
            [
                {
                    "question": "What is the largest planet in our solar system?",
                    "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                    "correct_answer": "Jupiter"
                },
                

                {
                    "question": "Who invented the telephone?",
                    "options": ["Alexander Graham Bell", "Albert Einstein", "Charles Darwin", "Rosalind Franklin"],
                    "correct_answer": "Alexander Graham Bell"
                },

                {
                    "question": "Which is not a form of carbon?",
                    "options": ["Diamond", "Graphite", "Amorphous Carbon", "Ferrite"],
                    "correct_answer": "Ferrite"
                },

                {
                    "question": "What is the lightest elemet in the periodic table?",
                    "options": ["Helium", "Hydrogen", "Carbon", "Nitrogen"],
                    "correct_answer": "Hydrogen"
                },

                {
                    "question": "What energy emerges from motion?",
                    "options": ["Potential Energy", "Electrical Energy", "Kinetic Energy", "Consistent Energy"],
                    "correct_answer": "Kinetic Energy"
                },
            
            ],
            #Hard Questions
            [
                {
                    "question": "Who proposed the theory of general relativity?",
                    "options": ["Albert Einstein", "Isaac Newotn", "Stephen Hawking", "Galileo Galilei"],
                    "correct_answer": "Albert Einstein"
                },
                

                {
                    "question": "What is the smallest planet in our solar system?",
                    "options": ["Saturn", "Venus", "Mercury", "Neptune"],
                    "correct_answer": "Mercury"
                },

                {
                    "question": "What is the chemical symbol for table salt?",
                    "options": ["S", "NaCl", "NH4F", "H2O"],
                    "correct_answer":"NaCl"
                },

                {
                    "question": "What is the normal pH level of human blood?",
                    "options": ["7.40", "5", "6.40", "2.3"],
                    "correct_answer":"7.40"
                },

                {
                    "question": "Which of the following planet was first discovered by the telescope?",
                    "options": ["Uranus", "Venus", "Jupitar", "Saturn"],
                    "correct_answer":"Uranus"
                },
            
            ]
        ]

        #Randomly select five questions from the selected difficulty level
        self.selected_questions = random.sample(question_banks[selected_difficulty], 5)

        self.questions = [q["question"] for q in self.selected_questions]
        self.correct_answers =[q["correct_answer"] for q in self.selected_questions]

        self.current_question_var = IntVar()
        self.current_question_var.set(1)

        self.question_label = Label(self.questionsframe, text=self.questions[0], font=("Times New Roman", 12), wraplength = 400, justify = "center") 
        self.question_label.grid (row=1, column=0, columnspan=3, padx=10, pady=10)

        self.options_var = StringVar()
        self.options_var.set(None)
        for i, option in enumerate(self.selected_questions[0]["options"]): #Puts the questions in order and can give the numbers to questions
            rb = Radiobutton(self.questionsframe, text=option, variable=self.options_var, value=option, font=("Times New Roman",10))
            rb.grid(row=i+2, column=1, columnspan=1, padx=10, pady=5, sticky=W)
            self.options_buttons.append(rb)

        self.submit_button = ttk.Button(self.questionsframe, text = "Submit", command=self.check_answer)
        self.submit_button.grid(row=7, column =0, columnspan=3, pady=10)

        self.feedback_label= Label(self.questionsframe, text = "", font=("Times New Roman", 12), wraplength=600, justify="center")
        self.feedback_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

#--------------------------------------------------------------- Function to the Check the Answers--------------------------------------------------------

    def check_answer(self):
        user_answer = self.options_var.get()
        current_question_index = self.current_question_var.get() - 1

        if user_answer:
            correct_answer = self.correct_answers[current_question_index]

            if user_answer == correct_answer:
                self.score += 1

            self.feedback_label.config(text=f"Your answer is {'correct!' if user_answer == correct_answer else 'incorrect!'}")
            self.current_question_var.set(current_question_index + 2)  # Move to the next question

        # Check if all questions are answered
            if current_question_index == len(self.questions) - 1:
                self.show_result()
            else:
                self.show_next_question()

    def show_next_question(self):
        current_question_index = self.current_question_var.get() - 1
        self.question_label.config(text=self.questions[current_question_index])

        for i, option in enumerate(self.selected_questions[current_question_index]["options"]):
            self.options_buttons[i].config(text=option, value=option) 
        
    


    #-----------------------------------------------------------Widget for Summary Frame------------------------------------------------------------------

          
        #Creating the SummaryFrame to print out the results/
        self.summaryframe = Frame(root, height = "200", width = "500", bg = "lightblue")

        #Creating list to of headings for SummaryFrame/
        summary_page = ["Name", "Gender", "Score"]
        self.summaryframe_labels = []

        for i in range(len(summary_page)):
            heading = Label(self.summaryframe, text = summary_page[i], anchor = W, width = "7", bg = "lightblue", font = ("Arial", "14", "bold"))
            self.summaryframe_labels.append(heading)
            heading.grid(row = 1, column = i+1, sticky = "EW")

        self.summaryname = Label(self.summaryframe, textvariable = self.name, bg = "lightblue")
        self.summaryname.grid(row = 3, column = 1, sticky = "EW")

        #Label for the users gender/
        self.summarygender = Label(self.summaryframe, textvariable = self.gender, bg = "lightblue")
        self.summarygender.grid(row = 3, column = 3, sticky = "EW")

        #Label for the users score/
        self.summaryscore = Label(self.summaryframe, text = "", bg = "lightblue")
        self.summaryscore.grid(row = 3, column = 4)







                   




             

        
        
        

            

        

        

        


    

        

        












#Main routine - This will run the script as the main module and the name of the parent window (root)
#__name__ is a variable defined for each script
if __name__ == "__main__":
    root = Tk()
    #This is the title of my GUI quiz
    root.title("Science Quiz 2023")
    GUI = ScienceQuiz(root)
    root.mainloop()
    
