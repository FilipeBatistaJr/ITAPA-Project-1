#ITAP PROJECT 1 LGYDZ146
#QUESTION 1

from tkinter import *

root = Tk()

root.title("Question 1")

item_list = [0, 0, 0]


def GUI ():

    def printItem_1():
        message = textbox_1.get()
        output = Label(root, text="item #1: R{message}")
        output.grid(row=5, column=0)
        item_1 = textbox_1.get()
        item_list[0] = int(item_1)
    
    def printItem_2():
        message = textbox_2.get()
        output = Label(root, text="item #2: R{message}")
        output.grid(row=6, column=0)
        item_2 = textbox_2.get()
        item_list[1] = int(item_2)
    
    def printItem_3():
        message = textbox_3.get()
        output = Label(root, text="item #3: R{message}")
        output.grid(row=7, column=0)
        item_3 = textbox_3.get()
        item_list[2] = int(item_3)

    def printPurchase():
        low_price = min(item_list)
        print("Lowest Price: R", low_price)
        output = Label(root, text="Lowest Price: Item #, {item_list.index(low_price) + 1}"
                                  "is the lowest price: R{low_price}")
        output.grid(row=8, coloumn=9)
        print(item_list)
        total_price = 0

        for i in range(3):
            total_price += item_list[i]

        print("Total price: R{total_price}")
        print("Discount price: R{total_price - low_price}")
        output_1 = Label(root, text="Total Price: R{total_price}")
        output_1.grid(row=9, coloumn=9)
        output_2 = Label(root, text="Disount price: R{total_price - low_price}")
        output_2.grid(row=10, coloumn=9)

    label_1 = Label(root, text="Item #1: R")
    textbox_1 = Entry(root)
    button_1 = Button(root, text="Add", COMMAND=printItem_1)

    label_2 = Label(root, text="Item #2: R")
    textbox_2 = Entry(root)
    button_2 = Button(root, text="Add", COMMAND=printItem_2)

    label_3 = Label(root, text="Item #3: R")
    textbox_3 = Entry(root)
    button_3 = Button(root, text="Add", COMMAND=printItem_3)

    label_1.grid(row=0, coloumn=0)
    label_2.grid(row=1, coloumn=0)
    label_3.grid(row=2, coloumn=0)

    textbox_1.grid(row=0, coloumn=3)
    textbox_2.grid(row=1, coloumn=3)
    textbox_3.grid(row=2, coloumn=3)

    button_1.grid(row=0, coloumn=7)       
    button_2.grid(row=1, coloumn=7) 
    button_3.grid(row=2, coloumn=7) 

    button_4 = Button(root, text="Confirm Purchase", command=printprintPurchase)
    button_4.grid(row=2, coloumn=8)

    root.mainloop()



#QUESTION 2

import random

# student_list = [] # Contains string representations of each student object
obj_list = [] # Contains student objects

class Student:
    def __init__(self, name, surname, age, student_id, cell_number, degree):
        self.name = name
        self.surname = surname
        self.age = age
        self.student_id = student_id
        self.cell_number = cell_number
        self.degree = degree

def registerStudent():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
    student_id = name[0:1] + surname[0:1] + str(age) + str(random.randint(0, 100))
    cell_number = input("Enter your cellphone number")
    degree = input("Enter your degree: ")

    new_student = Student(name, surname, age, student_id, cell_number, degree)

    obj_list.append((new_student.name, new_student.surname, new_student.age, new_student.student_id, new_student.cell_number, new_student.degree))

    # student_list.append(f"{name}, {surname}, {age}, {student_id}, {cell_number}, {degree}")

    print("Student ID: {new_student.student_id}\n"
          "Name:       {new_student.name}\n"
          "Surname:    {new_student.surname}\n"
          "Age:        {new_student.age}\n"
          "Cell No:    {new_student.cell_number}\n"
          "Degree:     {new_student.degree}")
    return name, surname, age, student_id, cell_number, degree

def getAllStudents():
    for i in range(len(obj_list)):
        print("Student #{i+1}: {obj_list[i]}")

def displayMainMenu():

    choice = input("\t---Menu---\n"
                   "1. Register a student\n"
                   "2. Display all registered students\n"
                   "3. Exit program\n")

    while choice:
        if choice == str(1):
            registerStudent()
            choice = input("\t---Menu---\n"
                           "1. Register a student\n"
                           "2. Display all registered students\n"
                           "3. Exit program\n")
        elif choice == str(2):
            getAllStudents()
            choice = input("\t---Menu---\n"
                           "1. Register a student\n"
                           "2. Display all registered students\n"
                           "3. Exit program\n")
        elif choice == str(3):
            break
            exit() # Terminate program
        else:
            print("invalid")
            choice = input()

def run():
    displayMainMenu()
    
class Graph():

    def __init__(self, cases, deaths, date):
        self.cases = cases
        self.deaths = deaths
        self.data = data

def Acquire_date():

    months = ["January", "Februaury", "March", "April", "May", "June", "July", "September","August", "October", "November", "December"]
    enter_year = int(input("Select the year between 2020 and 2021: "))
    if enter_year != 2020 and enter_year != 2021:
        print("Invalid")
    else:
        enter_month = input("Select a month: (e.g. March)\n")
        if enter_month not in months:
            print("Invalid")
        else:
            date = "{enter_month} {enter_year}"
            print(date)
            return date

import numpy as np
import matplotlib.pyblot as plt

#QUESTION 3
def Acquire_data():
    #NOTE: I only used the data on COVID-19 of South Africa only.
    # From the document available on mylms.
    # The data shows cases and deaths in 2020.

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    cases_2020 = [0, 0, 1353, 5467, 32683, 151209, 493183, 627041, 674339, 725452, 790004, 1057161]

    deaths_2020 = [0, 0, 5, 103, 683, 2657, 8005, 14149, 16734, 19276, 21525, 28469]

    def CvD_Graph_2020():
        x = (cases_2020[0], cases_2020[1], cases_2020[2], cases_2020[3], cases_2020[4])
        y = (deaths_2020[0], deaths_2020[1], deaths_2020[2], deaths_2020[3], deaths_2020[4])
        plt.plot(x,y)
        plt.xlabel("Cases")
        plt.ylabel("Deaths")
        plt.title("South Africa - 2020 Covid-19 Cases vs Deaths (Jan-May)")
        plt.show()

    def Graph_cases_2020():
        x = np.array(months)
        y = np.array(cases_2020)
        plt.plot(x,y)
        plt.xlabel("Nonths")
        plt.ylabel("Cases")
        plt.title("South Africa - 2020 Covid-19 Cases")
        plt.show()

CvD_Graph_2020()
Graph_cases_2020()

def runQ3():
    Acquire_data()
    
    
    
    
   