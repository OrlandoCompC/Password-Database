'''
Name: Orlando Companioni

This program is gonna check the strength of a password 
It will also store username and password in a file
It will be a menu based program that will allow the user to choose an option
Admin password is Password1
'''
import sys

def main():#This function will be the controller of the program
    process()

def menu(): #This function will display the menu options
    print()
    print("-------User Database--------")
    print(f"1. Show all user information")
    print(f"2. look up a user")
    print(f"3. Add a new user to the Database")
    print(f"4. Change a password")
    print(f"5. Delete a user")
    print(f"6. check password strength")
    print(f"7. Quit the program")
    print()

def menu_selection(): #This function will ask the user to select an option from the menu
    menu()
    #User input validation
    while True:
        try:
            option=int(input("Enter your option: "))
            if option not in range(1,8):
                print("ERROR: Enter a valid option") #if its a number but not in the range of 1 to 10
                continue
            break
        except ValueError:
            print("ERROR: Enter a numeric value") #if its not a number the program will ask the user to enter a number
            continue
    return option

def process(): #This function will process the user's choice
    createUsers()
    option=menu_selection() #The menu_selection function will return the user's choice as well as the menu
    while True:
        options={1:user_chart,2:user_LookUp,3:add_user,4:change_password,5:delete_user,6:password_check,7:quit}
        options[option]() #This will call the function that corresponds to the option chosen by the user
        option=menu_selection()

def quit(): #This function will quit the program
    print("Thank you for using the program")
    sys.exit()

def userValidation(username): #This function will validate the user's username
    with open("User_Database.txt", "r") as inventory:
        record = inventory.readline().rstrip()
        while record != "":
            fields = record.split(" ")
            if fields[0]==username:
                return True
            record = inventory.readline().rstrip()
    
def createUsers(): #This function will create a users at the start of the program
        username="JohnM123"
        password="Password123"
        with open("User_Database.txt", "w") as database:
            database.write(f"{username} {password}\n")

def admin(): #This function will ask the user for the admin password
    password=input("Enter the admin password: ")
    if password=="Password1":
        return True
    else:
        print("Incorrect password")
        return False

def user_chart(): #This function will display the inventory chart
    #Print table from the inventory myPersistentInventory.txt
    if admin():
        print()
        print(f"{'Username':<18}{'Password':18}")
        #reads line from the inventory and outputs it
        with open("User_Database.txt", "r") as inventory:
            record = inventory.readline().rstrip()
            while record != "":
                fields = record.split(" ")
                print(f"{fields[0]:<18}{fields[1]:<18}")
                record = inventory.readline().rstrip()
    else :print("You are not authorized to view this information")

def user_LookUp(): #This function will look up a user
    if admin():
        username=input("Enter the username: ")
        if userValidation(username):
            with open("User_Database.txt", "r") as inventory:
                record = inventory.readline().rstrip()
                while record != "":
                    fields = record.split(" ")
                    if fields[0]==username:
                        print(f"{fields[0]:<18}{fields[1]:<18}")
                        break
                    record = inventory.readline().rstrip()
                else:
                    print("User not found")
    else :print("You are not authorized to view this information")

def add_user(): #This function will add a user to the inventory
    username=input("Enter the username: ")
    if userValidation(username):
        print("Username already exists")
    else:
        while True:
            password=input("Enter the password: ")
            if valid_password(password):
                with open("User_Database.txt", "a") as database:
                    database.write(f"{username} {password}\n")
                break
            else:
                print("Please try again invalid password")
                continue

    
def change_password(): #This function will change a password
    username=input("Enter the username: ")
    if userValidation(username):
        while True:
            password=input("Enter the new password: ")
            if valid_password(password):
                with open("User_Database.txt", "r") as inventory:
                    record = inventory.readlines()
                    for lines in range(len(record)): #loops through the list
                        fields = record[lines].split(" ")
                        if username in fields:
                            record[lines]=f"{username} {password}\n"
                            break
                with open("User_Database.txt", "w") as database:
                    database.writelines(record)
                break
            else:
                print("Please try again invalid password")
                continue
    else:print("User not found")
            

def delete_user(): #This function will delete a user
    if admin():
        username=input("Enter the username: ")
        if userValidation(username):
            with open("User_Database.txt", "r") as inventory:
                record = inventory.readlines()
                for lines in range(len(record)):
                    fields = record[lines].split(" ")
                    if username in fields:
                        del record[lines] #deletes the line from the list
                        print("User deleted")
                        break
            with open("User_Database.txt", "w") as inventory:
                inventory.writelines(record)
        else:print("User not found")

def password_check(): #This function will check the strength of a password
    user_password=input(f"Please enter a password: ")
    valid_password(user_password)
    
def valid_password(user_password): #This function will check if the password is valid
    symbol_list= ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","'","?""<",">"]
    #symbol_list has a list of symbols a user might use
    
    valid_pass=1   #turns 0 when the password is invalid in any way
    pass_length=len(user_password)

    # If the password doesnt contain letters then it becomes 0
    contains_letter=1
    
    #did not use nested ifs because i wanted it to check all conditions and tell the user what they needed to add

    if pass_length<=12: # checks if the length of the password is less than or equal to 12
        valid_pass = 0   
        print(f"Invalid password. Password length must be at least 12 characters long.")
              
    # The not operator makes it so that if it doesnt have a digit then it executes
    if not any(char.isdigit() for char in user_password):
        #it iterates through the password checking if it has digits

        valid_pass=0
        print(f"Invalid password. Password must contain at least 1 number")

    if not any(char.isalpha() for char in user_password):
        valid_pass=0
        contains_letter=0
        print(f"Invalid password. Password must contain at least 1 letter")
        
    if not any(char in symbol_list for char in user_password):
        # in this case it compares characters in a list to those the password
        valid_pass=0
        print(f"Invalid password. Password must contain at least 1 symbol")      

    if not any(char.isupper() for char in user_password) and contains_letter==1:
        # if it doesnt contain letters then it doesnt execute because only letters can be upper or lowercase
        valid_pass=0

        print("Invalid password. Password must contain at least 1 uppercase letter")
          
    if not any(char.islower() for char in user_password) and contains_letter==1:
        valid_pass=0
        print("Invalid password. Password must contain at least 1 lowercase letter")
        
    if valid_pass==1:# if its still valid then it prints that it is
        print(f"The Password is valid")
        return True
    
try:
    if __name__ == "__main__": #This will run the main function
        main()
except KeyboardInterrupt:
    print("Program terminated by user") #This will catch a keyboard interrupt and print a message