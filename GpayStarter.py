
from GpayController import *

obj = GpayController()
while True:
    print("\n\n**************************")
    print("1 --> Signup")
    print("2 --> Login")
    print("3 --> Exit")
    print("*************************")
    option = int(input("Choose your prefered option:"))
    if option == 1:
        obj.handleSignup()
    elif option == 2:
        obj.handleLogin()
    elif option == 3:
        print("Thank You For Choosing Gpay!!!")
        exit(0)
    else:
        print("select appropriate option")
