#Created on 1st March, 2020
#Copyright TARS Inc.
#Made with ❤ in Mary's 
from openpyxl import Workbook
from add import adder
from mark import marker
from view import tview
from remove import remo
import os

def asker():
    x = input("Do you wish to continue using the app? (1-Yes, 0-No): ")
    return x
    

def dev_manner(dam):
    
    xc = 0
    while(xc==0):
        print("Your classes-")
        mp = os.path.abspath('../')
        path = mp+"/sub/"+dam+"/"+"subs.txt"
        lines = tuple(open(path).read().split('\n'))
        ran = len(lines)
        
        for x in range(1,ran):
            y=str(x)
            x=x-1
            x=str(lines[x])
            print(y+". "+x)
        
        mans = input("Select class (number): ")
        mans = int(mans)

        if(mans>=1 and mans<ran):
            mans = mans-1
            answer = lines[mans]
            answer = str(answer)
            xc=1
        else:
            xc=0
            print("\nInvalid input. Please try again.\n")
        



    val=1
    while(val==1):
        gam = dam
        print("\nClass selected: "+answer)
        print("\n")
        print("1.)Change class 2.)Add students 3.)Remove students 4.)Mark attendance 5.)View attendance 6.)LOGOUT")

        inp = input("Enter option (1-4):")

        if(inp=='1'):
            dev_manner(gam)
        if(inp=='2'):
            #Function call to add students to list
            adder(gam,answer)
            y=asker()

        elif(inp=='3'):
            #Function call to remove student from list
            remo(gam,answer)
            y=asker()

        elif(inp=='4'):
            #Function call to mark attendance of students
            marker(gam,answer)
            y=asker()

        elif(inp=='5'):
            #Function call to view attendance
            tview(gam,answer)
            y=asker()
            print(y)


        elif(inp=='6'):
            #Function call to logout from the service.
            print("\n")
            print("You have successfully logged out.")
            exit()
            


        else:
            #Function call to print error message and restart program
            print("Incorrect choice. Please try again.")

            #Ticket - add the option to restart program again.
        val=int(y)
