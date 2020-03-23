#This is the hub for all the python files/sections.
#Copyright TARS Inc.
#Made with ❤ in Mary's 

import getpass
from dec import reg
from register import regie

def homie():
    print("hello")
    print("\n")
    print("#############################################")
    print("##                                         ##")
    print("##                 TARS                    ##")
    print("##            ATTENDANCE APP               ##")
    print("##                                         ##")
    print("#############################################")
    print("Made with ❤ in Mary's")

    print("\n") 
    choi = input("1. LOGIN | 2. REGISTER : ")
    if(choi=='1'):
        uid = input("Username: ")
        pwd = getpass.getpass("Password: ")
        reg(uid,pwd)
    else:
        regie()
homie()




