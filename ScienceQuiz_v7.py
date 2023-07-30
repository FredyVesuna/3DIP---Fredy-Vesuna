#ScienceQuiz_v7.py
#Multi-choice science quiz for primary to high-school students (ages 6-18) with 3 levels of difficulties
#Fredy Vesuna, 25/07/2023


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


class ScienceQuiz:
    def __init__(self, parent):
#-------------------------------------------------------#
        self.options_buttons = []
        self.informationframe = None  
        self.questionsframe = None
        self.summaryframe = None
        
        self.name_value = StringVar()
        self.age_value = StringVar()
        self.gender_value = StringVar()
        self.difficulty_level = StringVar()

#-------------------------------------------------------#
        
#----------------------------------------------------------------- Configuring the Widgets for HomeFrame -------------------------------------------------------------#
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def show_information_frame(self):
#-------------------------------------------------------#
        if self.questionsframe:
            self.questionsframe.destroy()
        if self.informationframe:
            self.informationframe.destroy()

        self.options_buttons.clear()
        
        if self.homeframe:
            self.homeframe.grid_forget()
#-------------------------------------------------------#

#--------------------------------------------------------- Configuring the Widgets for InformationFrame -------------------------------------------------------------#        
        self.informationframe = Frame(root)
        self.informationframe.grid(row=0, column=0)

        self.headinglabel = Label(self.informationframe, bg = "light green", fg = "black", width = 40, padx = 40, pady = 20, text = "ENTER YOUR INFORMATION", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(columnspan = 5)
        
        self.namelabel = Label(self.informationframe, text = " Enter your first name:", width = 60, font = ("Calibri", "11", "bold"))
        self.namelabel.grid(row = 2, column = 0, sticky = N)

        self.name = StringVar()
        self.name.set("")
        self.nameentry = ttk.Entry(self.informationframe, textvariable = self.name_value, width = 25)#The text box for the user to enter their name with ttk/
        self.nameentry.grid(row = 3, column = 0, sticky = N)

        self.agelabel = Label(self.informationframe, text = "Enter your age:", width = 21, font = ("Calibri", "11", "bold"))
        self.agelabel.grid(row = 4, column = 0, sticky = N,)

        self.age = StringVar()
        self.age.set("")
        self.ageentry = ttk.Entry(self.informationframe, width = 25, textvariable = self.age_value)
        self.ageentry.grid(row = 5, column = 0, sticky = N)

        self.genderlabel = Label(self.informationframe, text = "Enter your gender:", width = 24, font = ("Calibri", "11", "bold"))
        self.genderlabel.grid(row = 6, column = 0, sticky = N)

        select_gender = ["Male", "Female", "Other"]

        self.gender = ttk. Combobox (self.informationframe, values = select_gender, width = 22, state = "readonly", textvariable=self.gender_value)
        self.gender.grid(row = 7, column = 0, sticky = N)

        self.difficultylabel = Label(self.informationframe, text = "Which difficulty would you like to choose:", width = 55, padx = 60, pady = 10, font = ("Times New Roman", "16", "bold underline"))
        self.difficultylabel.grid(row = 12, column = 0, sticky = N)

        self.difficulty = ["Easy Quiz", "Medium Quiz", "Hard Quiz"]
        self.difficulty_level = StringVar()
        self.difficulty_level.set(0)
        self.difficulty_buttons = []

         
        for i in range (len(self.difficulty)):
            button = ttk.Radiobutton(self.informationframe, variable = self.difficulty_level, value = i, text = self.difficulty[i], width = "40")
            self.difficulty_buttons.append(button)
            button.grid(row = i+14, column = 0, sticky = N)

        self.submit = ttk.Button(self.informationframe, text="Proceed to the Questions!", command= self.show_questions_frame)
        self.submit.grid(row=20, column=0)

        self.back_to_home_button = ttk.Button(self.informationframe, text="Back to Home", command=self.show_home_frame)
        self.back_to_home_button.grid(row=21, column=0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        
#-------------------------------------------------------- Configuring Method to Check User's Information -------------------------------------------------------------#
    def validate_input(self):
        name = self.name_value.get().strip()
        age = self.age_value.get().strip()
        gender = self.gender_value.get()

        if not name:
            messagebox.showerror("Input Error", "Error: Please enter a valid name.")
            return False

        if not name.isalpha():
            messagebox.showerror("Input Error", "Error: Name can only contain letters.")
            return False

        if not age:
            messagebox.showerror("Input Error", "Error: Please enter your age.")
            return False

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Error: Please enter a valid age.")
            return False

        if age < 6 or age > 18:
            messagebox.showerror("Input Error", "Error: You are too young or too old to particpate.")
            quit()

        if not gender:
            messagebox.showerror("Inputer Error", "Error: Please select your gender.")
            return False
        
        return True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------- Configuring Method to Show Questions Frame ------------------------------------------------------#
    def show_questions_frame(self):
        if not self.validate_input():
            return

        if self.informationframe:
            self.informationframe.destroy()
        if self.questionsframe:
            self.questionsframe.destroy()

        if self.homeframe:
            self.homeframe.grid_forget()


        self.questionsframe = Frame(root, padx=20, pady =20)
        self.index = 0
        self.score = 0
        self.questionsframe.grid(row=0, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------- Configuring the Widgets for QuestionFrame ----------------------------------------------------#
        self.headinglabel = Label(self.questionsframe, bg = "lightgrey", fg = "green", width = 50, padx = 40, pady = 20, text = "SCIENCE QUIZ QUESTIONS", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(row = 0, columnspan = 3)
        
#--------------------------------------------------------------------------------------------------------------------
        selected_difficulty = int(self.difficulty_level.get())

        question_banks = [
           
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

        self.selected_questions = random.sample(question_banks[selected_difficulty], 5)

        self.questions = [q["question"] for q in self.selected_questions]
        self.correct_answers =[q["correct_answer"] for q in self.selected_questions]

        self.current_question_var = IntVar()
        self.current_question_var.set(1)

        self.question_label = Label(self.questionsframe, text=self.questions[0], font=("Times New Roman", 12), wraplength = 400, justify = "center") 
        self.question_label.grid (row=1, column=0, columnspan=3, padx=10, pady=10)

        self.options_var = StringVar()
        self.options_var.set(None)
        for i, option in enumerate(self.selected_questions[0]["options"]):
            rb = Radiobutton(self.questionsframe, text=option, variable=self.options_var, value=option, font=("Times New Roman",10))
            rb.grid(row=i+2, column=1, columnspan=1, padx=10, pady=5, sticky=W)
            self.options_buttons.append(rb)

#----------------------------------------------------------------------------------------------------------------------------
        self.submit_button = ttk.Button(self.questionsframe, text = "Submit", command=self.check_answer)
        self.submit_button.grid(row=7, column =0, columnspan=3, pady=10)

        self.feedback_label= Label(self.questionsframe, text = "", font=("Times New Roman", 12), wraplength=600, justify="center")
        self.feedback_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        self.back_to_information_button = ttk.Button(self.questionsframe, text="Back to Information", command=self.show_information_frame)
        self.back_to_information_button.grid(row=8, column=1)

        self.back_to_home_button = ttk.Button(self.questionsframe, text="Back to Home", command=self.show_home_frame)
        self.back_to_home_button.grid(row=9, column=1)
#-----------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------- Configuring Method to the Check User's Answers -----------------------------------------------------------#
    def check_answer(self):
        user_answer = self.options_var.get()
        current_question_index = self.current_question_var.get() - 1

        if user_answer:
            correct_answer = self.correct_answers[current_question_index]

            if user_answer == correct_answer:
                self.score += 1

            self.feedback_label.config(text=f"Your answer is {'correct!' if user_answer == correct_answer else 'incorrect!'}")
            self.feedback_label.grid(row = 8, column = 2)
            self.current_question_var.set(current_question_index + 2)  # Move to the next question

    
            if current_question_index == len(self.questions) - 1:
                self.show_summary_frame()
            else:
                self.show_next_question()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------- Configuring Method for User to Move on to Next Question ----------------------------------------------------#
    def show_next_question(self):
        current_question_index = self.current_question_var.get() - 1
        self.question_label.config(text=self.questions[current_question_index])

        #Destroy the old radio buttons (if any) for the restart
        for rb in self.options_buttons:
            rb.destroy()

        self.options_buttons.clear()


        for i, option in enumerate(self.selected_questions[current_question_index]["options"]):
            rb = Radiobutton(self.questionsframe, text=option, variable=self.options_var, value=option, font=("Times New Roman", 10))
            rb.grid(row=i + 2, column=1, columnspan=1, padx=10, pady=5, sticky=W)
            self.options_buttons.append(rb)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------- Configuring Widgets for the SummaryFrame ----------------------------------------------------------------#
    def show_summary_frame(self):
        if self.questionsframe:
            self.questionsframe.destroy()

        if self.summaryframe:
            self.summaryframe.destroy()

        self.summaryframe = Frame(root, padx=20, pady=20)
        self.summaryframe.grid(row=0, column=0)

        summary_page = ["Name", "Age", "Gender", "Score"]
        self.summaryframe_labels = []

        for i in range(len(summary_page)):
            heading = Label(self.summaryframe, text=summary_page[i], anchor=W, width=15, bg="lightblue", font=("Arial", 14, "bold"))
            self.summaryframe_labels.append(heading)
            heading.grid(row=1, column=i, sticky="EW")

        self.summary_name = Label(self.summaryframe, text=self.name_value.get(), bg="lightblue")
        self.summary_name.grid(row=3, column=0, sticky="EW")

        self.summary_age = Label(self.summaryframe, text=self.age_value.get(), bg="lightblue")
        self.summary_age.grid(row=3, column=1, sticky="EW")

        self.summary_gender = Label(self.summaryframe, text=self.gender_value.get(), bg="lightblue")
        self.summary_gender.grid(row=3, column=2, sticky="EW")

        self.summary_score = Label(self.summaryframe, text=str(self.score) + "/5", bg="lightblue")
        self.summary_score.grid(row=3, column=3, sticky="EW")

        self.restart_button = ttk.Button(self.summaryframe, text="Restart Quiz", command=self.restart_quiz)
        self.restart_button.grid(row=4, column=1, padx=5, pady=10)

        self.quit_button = ttk.Button(self.summaryframe, text="Quit", command=self.quit_quiz)
        self.quit_button.grid(row=4, column=2, padx=5, pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------- Configuring Method to allow User to Go Back -------------------------------------------------------------#
    def show_home_frame(self):
        if self.questionsframe:
            self.questionsframe.destroy()
        if self.informationframe:
            self.informationframe.destroy()
        if self.homeframe:
            self.homeframe.grid(row=0, column=0)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------- Configuring Methods to allow User to Restart or Quit the Quiz ----------------------------------------------#

    def restart_quiz(self):
        if self.summaryframe:
            self.summaryframe.destroy()

        # Reset all variables
        self.name_value.set("")
        self.age_value.set("")
        self.gender_value.set("")
        self.difficulty_level.set(0)

        # Reset radio button selection
        self.difficulty_level.set(None)
        
        # Destroy questionsframe and informationframe if they exist
        if self.questionsframe:
            self.questionsframe.destroy()
        if self.informationframe:
            self.informationframe.destroy()

        # Go back to the homeframe
        self.show_home_frame()

    def quit_quiz(self):
        root.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            

#Main routine - This will run the script as the main module and the name of the parent window (root)
#__name__ is a variable defined for each script
if __name__ == "__main__":
    root = Tk()
    #This is the title of my GUI quiz
    root.title("Science Quiz 2023")
    GUI = ScienceQuiz(root)
    root.mainloop()
    
