#Created on 1st March, 2020
#Copyright TARS Inc.
#Made with ❤ in Mary's 

from openpyxl import Workbook
from add import adder
from mark import marker
from view import tview

def dev_manner():
    print("\n")
    print("LOGIN SUCCESSFUL. Welcome to Attendance app!")
    print("\n")
    print("1.)Add students 2.)Remove students 3.)Mark attendance 4.)View attendance")

    inp = input("Enter option (1-4):")


    if(inp=='1'):
        #Function call to add students to list
        adder()

    elif(inp=='2'):
        #Function call to remove student from list
        print("Option to remove student")
        print("This feature is under works. Please check later :)")

    elif(inp=='3'):
        #Function call to mark attendance of students
        marker()

    elif(inp=='4'):
        #Function call to view attendance
        tview()

    elif(inp=='5'):
        #Function call to logout from the service.
        print("\n")
        print("You have successfully logged out.")
        m_scr()


    else:
        #Function call to print error message and restart program
        print("Incorrect choice. Please try again.")

        #Ticket - add the option to restart program again.
