
#This is the hub for all the python files/sections.
#Copyright TARS Inc.

import getpass
from main import dev_manner


print("\n")
print("#############################################")
print("##                                         ##")
print("##                 TARS                    ##")
print("##            ATTENDANCE APP               ##")
print("##                                         ##")
print("#############################################")

ids = ["noor","kayal","anu"]
secu = "rootmin"
print("\n") 
print("LOGIN-")

uid = input("Username: ")
pwd = getpass.getpass(prompt="Password: ")

for i in ids:
    if(uid==i):
        if(pwd==secu):
            dev_manner()
        else:
            print("Sorry, wrong credentials :(")

