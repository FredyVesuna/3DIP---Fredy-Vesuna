#ScienceQuiz_v1.py
#Science quiz for all ages with 3 levels of difficulties
#Fredy Vesuna, 26/06/2023

#This is the standard python interface tk GUI
from tkinter import *

from tkinter import ttk
#This module provides access to the Tk themed widget set. This gives a better look and feel to make the GUI asetheically pleasing for the user 

#This will generate the questions in a random order
import random


#Defining science quiz GUI
class ScienceQuiz:

#__init__ is known as a constructor in onject oriented programming. It is a concept to initalize the attributes of a class (sciencequiz)
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


#----------------------------------------------------------------- Widgets for Information Frame ---------------------------------------------------------------------------

        
        self.informationframe = Frame(parent, heigh = "450", width = "600")




        #Button
        self.submit = ttk.Button(self.homeframe, text = "Participate and Enter Your Details!", command = self.informationframe)
        self.submit.grid(row = 11, column = 1)
        
        

        
   















#Main routine - This will run the script as the main module and the name of the parent window (root)
#__name__ is a variable defined for each script
if __name__ == "__main__":
    root = Tk()
    #This is the title of my GUI quiz
    root.title("Science Quiz 2023")
    GUI = ScienceQuiz(root)
    root.mainloop()
    
