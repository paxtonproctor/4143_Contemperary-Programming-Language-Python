# Paxton Proctor
# Programassignment2
# Problem 1
# CMPS-4143-101 Top: Cont Programming Language
# 11/8/2021
# (35 points) Write a Python program using file operation. You will open an input file
# “students.dat” that will contain a list of student names, classification, and grade in the
# class. (All student info is completely made up) You should read through the entire input
# file. After reading in all information, do operations (No built-in functions like Average,
# min, max, count, etc.), close the input file and write that following information with
# labels to an output file “student_statistics.txt”

#Attempting to open file for reading only and will throw a exception if it can't open
try:
    Infile = open('students.dat', 'r')
except:
    raise OSError("Sorry could not open the file try again")
#Attempting to open a file for writing and will throw a exception if it can't open
try:
    Outfile = open('student_statistics.txt', 'w')
except:
    raise OSError("Sorry could not open the file try again")

# continue if file works
with Infile:
    # initialization
    HighestGrade = 0
    LowestGrade = 0
    ClassAvg = 0
    NumFresh = 0
    NumSoph = 0
    NumJun = 0
    NumSen = 0
    NumLines = 0
    bool = True

    #reading in each line
    for line in Infile:
        # gets the elements from whitespace
        Element = line.strip().split(' ')

        # gets the first and last element
        FirstName = str(Element[0])
        LastName = str(Element[1])

        # Takes the sum of all the different classes
        if Element[2].lower() == 'freshman':
            NumFresh += 1
        elif Element[2].lower() == 'sophmore':
            NumSoph += 1
        elif Element[2].lower() == 'junior':
            NumJun += 1
        elif Element[2].lower() == 'senior':
            NumSen += 1

        grade = int(Element[3])
        if bool:
            LowestGrade = grade
            HighestGrade = grade
            bool = False
        else:
            # gets highest grade
            if grade > HighestGrade:
                HighestGrade = grade
                First_Name = FirstName
                Last_Name = LastName
            # gets the lowest grade
            if grade < LowestGrade:
                LowestGrade = grade
                First__Name = FirstName
                Last__Name = LastName
        ClassAvg += grade

        NumLines += 1
# print to file
Outfile.write('\rStudent with the Highest grade in the class and congrats for being the smartest one in class  :  '+ First_Name + " "+ Last_Name)
Outfile.write('\rHighest grade in the class because someone was either a try hard or very lucky                :  ' + str(HighestGrade))
Outfile.write('\rThe Lowest Grade in the class because good god this grade is apparently low                   :  ' + str(LowestGrade))
Outfile.write('\rStudent with the Worst grade in the class and should probably drop out and live a better life :  '+ First__Name + " "+ Last__Name)
# round to two decimal places
Outfile.write('\rThe Class Average Was             :  %.2f'%(ClassAvg / NumLines))
Outfile.write('\rTotal of freshmen students   : ' + str(NumFresh))
Outfile.write('\rTotal of Sophomores students : ' + str(NumSoph))
Outfile.write('\rTotal of Juniors students    : ' + str(NumJun))
Outfile.write('\rTotal of Seniors students    : ' + str(NumSen) + '\r\n')

# Closing the input and output file.
Outfile.close()
Infile.close()       