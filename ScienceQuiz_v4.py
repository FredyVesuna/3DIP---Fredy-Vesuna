#ScienceQuiz_v1.py
#Science quiz for all ages with 3 levels of difficulties
#Fredy Vesuna, 22/07/2023

#This is the standard python interface tk GUI
from tkinter import *

from tkinter import ttk
#This module provides access to the Tk themed widget set. This gives a better look and feel to make the GUI asethetically pleasing for the user 

#This will generate the questions in a random order
import random


#Defining science quiz GUI
class ScienceQuiz:

#__init__ is known as a constructor in object oriented programming. It is a concept to initalize the attributes of a class (sciencequiz)
#"self" is a variable that must be the prefix to all variables that will belong to the instances of the class
    def __init__(self, parent):

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

        self.age = IntVar()
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

         #For loop/
        for i in range (len(self.difficulty)):
            button = ttk.Radiobutton(self.informationframe, variable = self.difficulty_level, value = i, text = self.difficulty[i], width = "40")
            self.difficulty_buttons.append(button)
            button.grid(row = i+14, column = 0, sticky = N)
        
        self.submit = ttk.Button(self.informationframe, text="Proceed to the Questions!", command= self.showquestionsframe)
        self.submit.grid(row=20, column=0)



#----------------------------------------------------------------- Widgets for Questions Frame ---------------------------------------------------------------------------

   
    def showquestionsframe(self):
        self.informationframe.destroy()
        self.questionsframe = Frame(root)
        self.index = 0
        self.score = 0
        self.questionsframe.grid(row=0, column=0)

        self.headinglabel = Label(self.questionsframe, bg = "lightgrey", fg = "green", width = 85, padx = 40, pady = 20, text = "SCIENCE QUIZ QUESTIONS", font = ("Times New Roman", "16", "bold"))
        self.headinglabel.grid(row = 0, columnspan = 3)

    

        #Empty Label for the questions that will be configured later/
        self.questionslabel = Label(self.questionsframe, width = 60, height = 3, fg = "yellow", font = ("Times New Roman", "12", "bold"))
        self.questionslabel.grid(row = 1, column = 0, sticky = N)

        self.answersentry = ttk.Entry(self.questionsframe, width = 30)
        self.answersentry.grid(row = 2, column = 0, sticky = N)

         #Empty label for feedback which will be configured later/
        self.answerfeedback = Label(self.questionsframe, width = 40)
        self.answerfeedback.grid(row = 1, column = 1, sticky = E)


         #Button for the user to access the HomeFrame again/
        self.homepage = ttk.Button(self.questionsframe, text = "Reset and return to Home Page", command = self.reset)
        self.homepage.grid(row = 11, column = 2, sticky = E)

        #Button for the user to check their answer/
        self.checkanswer = ttk.Button(self.questionsframe, text = "Check Answer", command = self.Answers)
        self.checkanswer.grid(row = 2, column = 1, sticky = N)






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

        #Button for the user to redo quiz/
        self.GUIReset = ttk.Button(self.summaryframe, text = "Go back and try again!", command = self.reset)
        self.GUIReset.grid(row = 5, column = 4, sticky = N)

        #Button for user to quit programme/
        self.quit = ttk.Button(self.summaryframe, text = "Exit the Science Quiz", command = quit)
        self.quit.grid(row = 5, column = 1, sticky = W)

        
        
        

            

        

        

        


    

        

        














#Main routine - This will run the script as the main module and the name of the parent window (root)
#__name__ is a variable defined for each script
if __name__ == "__main__":
    root = Tk()
    #This is the title of my GUI quiz
    root.title("Science Quiz 2023")
    GUI = ScienceQuiz(root)
    root.mainloop()
    
