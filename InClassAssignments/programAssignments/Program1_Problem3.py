# Paxton Proctor
# Programassignment1
# Problem 3
# CMPS-4143-101 Top: Cont Programming Language
# 10/23/2021
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
# integer (similar to C/C++'s atoi function). (40 points)
# The algorithm for myAtoi(string s) is as follows:
# a) Read in and ignore any leading whitespace.
# b) Check if the next character (if not already at the end of the string) is '-' or '+'. Read
# this character in if it is either. This determines if the final result is negative or positive
# respectively. Assume the result is positive if neither is present.
# c) Read in next the characters until the next non-digit character or the end of the input
# is reached. The rest of the string is ignored.
# d) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits
# were read, then the integer is 0. Change the sign as necessary (from step 2).
# e) If the integer is out of the 32-bit signed integer range [-2
# 31, 231 - 1], then clamp
# the integer so that it remains in the range. Specifically, integers less than -2
# 31 should
# be clamped to -2
# 31, and integers greater than 2
# 31 - 1 should be clamped to 2
# 31 - 1.
# f) Return the integer as the final result.

# definition function
def myAtoi(s):
    InString = ""
    positiveNum = True

    # checks to see if the input of the string is 0
    if len(s) == 0:
        return 0

    i = 0
    # ignore white spaces
    while i < len(s):
        if s[i] != " ":
            break
        i+=1
    
    if i < len(s):
        # check for values 0-9
        if ord('0') <= ord(s[i]) <= ord('9'):
            InString += s[i]
        # if sign is negative
        elif s[i] == "-":
            positiveNum = False
        # if sign is positive
        elif s[i] == "+":
            pass
        else:
            return 0

    i+=1

    # run till end of loop
    while i < len(s):
        if ord('0') <= ord(s[i]) <= ord('9'):
            InString += s[i]
    
        else:
            break
        i+=1

    # checking for 32 bit conversion
    if len(InString)==0:
        return 0
    else:
        if positiveNum:
            return min(int(InString), 2**31-1)
        return max(-1*int(InString), -2**31)
    
try:
    s = str(input("\nEnter some input: "))                                    
    myAtoi(s)                     

except:
    print("Error, invalid data unable to process")                           


print('Input:    "',s,'"',"\t\t",'OutPut:    ',myAtoi(s.lstrip()),'\n')     
    

