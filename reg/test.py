#This is the hub for all the python files/sections.
#Copyright TARS Inc.
#Made with ❤ in Mary's 

import sys
sys.path.insert(0,'C:/Users/Abhay Ram/Desktop/tars-att/reg-test/')
import getpass
from dec import reg
from register import install



def overv():
    print("\n")
    print("#############################################")
    print("##                                         ##")
    print("##                 TARS                    ##")
    print("##            ATTENDANCE APP               ##")
    print("##                                         ##")
    print("#############################################")
    print("Made with ❤ in Mary's")

    print("\n") 
    print("hey")
    choi = input("1. LOGIN | 2. REGISTER")
    if(choi==1):
        uid = input("Username: ")
        pwd = getpass.getpass(prompt="Password: ")
        reg(uid ,pwd)
    elif(choice==2):
        install()

overv()



