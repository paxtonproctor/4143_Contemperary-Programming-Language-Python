# Paxton Proctor
# Programassignment1
# Problem 2
# CMPS-4143-101 Top: Cont Programming Language
# 10/23/2021
# Write a program where it asks to enter the number of people, then based on this number
# iterate that amount of time where each time get single person’s information like First Name,
# Last Name, Age, Occupation and Address. Make sure you validate all users’ input. Included but
# not limited to like age cannot be a non-numeric value should be between 0-150, name can only
# be non-numeric. You need to think how you can validate the occupation and address field.
# Finally show (print) user details one by one. For your input validation, make sure you can’t
# proceed next step/value without inserting valid input on current phase.

def FirstName():
    while (True):
            First_Name = str(input('What is your first name?'))

            if First_Name.isnumeric():
                print('You have not entered a string value try again')
                FirstName()

            else:
                break

def LastName():
    Last_Name = str(input('What is your Last name?'))

    if Last_Name.isnumeric():
        print('You have not entered a string value try again')
        LastName()

    else:
        print(Last_Name)
        return

def Age():

    age = input('What is your Age?')
    
    age = int(age)

    if age < 120:
        print('You have not entered a correct age try again')
        Age()
    
    age = str(age)
    if not age.isnumeric():
        print('You have not entered a correct age try again')
        Age()
    else:
        print(age)
        return        
# ask user for number of people
print('Give how many people would you like to add?')

# declarations
i = 0
x = int(input())
# start of while
while i < x:
    FirstName()
    LastName()
    Age()
    #bool = 0
    #while bool == 0:
            #FirstName = str(input('What is your first name?'))

            #if FirstName.isnumeric():
                #print('You have not entered a string value')

            #else:
                #bool = 1
    
    #while bool == 1:
            #LastName = str(input('What is your Last name?'))
            
            #if LastName.isnumeric():
                #print('You have not entered a string value')
            #else:
                #bool = 0
    i+=1
