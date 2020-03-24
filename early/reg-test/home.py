import getpass
from dec import reg
from register import regie

def homie():
    print("#############################################")
    print("##                 TARS                    ##")
    print("##            ATTENDANCE APP               ##")
    print("#############################################")
    print("Made with ❤ in Mary's")

    
    print("\n") 
    choi = input(" 1. LOGIN \n 2. REGISTER \n\nEnter option: ")
    
    if(choi=='1'):
        uid = input("Username: ")
        pwd = getpass.getpass("Password: ")
        reg(uid,pwd)
    elif(choi=='2'):
        v = regie()
        if(v==0):
            homie()
    else:
        print("\nSorry, wrong input :/")
        print("Please try again!")
        homie()
        
homie()




