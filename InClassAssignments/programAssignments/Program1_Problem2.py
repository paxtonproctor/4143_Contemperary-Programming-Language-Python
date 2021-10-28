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

# function name
def FirstName():
    
    # checking to see if its a numeric value
    if first_Name.isnumeric():
        print('You have not entered a string value try again')
        FirstName()
    # print name
    else:
        print(first_Name)
        return first_Name

# function name
def LastName():
    # checking to see if its a numeric value
    if Last_Name.isnumeric():
        print('You have not entered a string value try again')
        LastName()

    # print name
    else:
        print(Last_Name)
        return

# Function name
def Age():
    # cheking to see if age is good
    if age > 120:
        print('You have not entered a correct age try again')
        Age()
    elif age < 0:
        print('You have not entered a correct age try again')
        Age()
    else:
        print(age)
        return 

# function name
def Occupation():
    # checking to see if its a numeric value
    if occupation.isnumeric():
        print('You have not entered a string value try again')
        Occupation()

    # print name
    else:
        print(occupation)
        return

# function name
def Address():
    print(address)
    return

# function name
def City():
    # checking to see if its a numeric value
    if city.isnumeric():
        print('You have not entered a string value try again')
        City()

    # print name
    else:
        print(city)
        return

# function name
def State():
    # checking to see if its a numeric value
    if state.isnumeric():
        print('You have not entered a string value try again')
        State()

    # print name
    else:
        print(state)
        return

def ZipCode():
    # cheking to see if age is good
    if len(zipcode) < 5:
        print('You have not entered a correct zipcode try again')
        ZipCode()
    elif len(zipcode) > 5:
        print('You have not entered a correct zipcode try again')
        ZipCode()
    else:
        print(zipcode)
        return zipcode

# ask user for number of people
print('Give how many people would you like to add?')

# declarations
i = 0
x = int(input())
# start of while
while i < x:
    # asking for input string
    first_Name = str(input('What is your First name?'))
    # asking for input string
    Last_Name = str(input('What is your Last name?'))
    # asking for integer age
    age = int(input('What is your Age?'))
    # asking for input string
    occupation = str(input('What is your Occupation?'))
    # asking for input string
    address = input('What is your Address?')
    # asking for input string
    city = str(input('What is your city?'))
    # asking for input string
    state = str(input('What is your state?'))
    # asking for integer age
    zipcode = input('What is your zipcode?')

    # calling functions
    FirstName()
    LastName()
    Age()
    Occupation()
    Address()
    City()
    State()
    ZipCode()

    # format the output for each individual person to be this  formatted
    print(first_Name, Last_Name, " aged", age," years, worked as a ",occupation,
             " and currently lives at ",address, "", city, "," ,state, " ", zipcode,".\n")
    i+=1
