# Paxton Proctor
# Programassignment3
# Problem 2
# CMPS-4143-101 Top: Cont Programming Language
# 11/16/2021
# Find if an expression has duplicate parenthesis

# function for finding the duplicates
def Dup(exp):
    
    if not exp or len(exp) <= 4:
        return False

    # create a Stack of characters
    Stack = []

    # for every character in expression check to see if it is ()
    for ch in exp:
        # if the current char isn't ) then skip otherwise append when closing
	    if ch != ')':
		    Stack.append(ch)
		# if the current char in the expression is a closing parenthesis
	    else:
			# if the Stack's top element is an opening parenthesis,
			# the subexpression of the form ((exp)) is found
		    if Stack[-1] == '(':
			    return True

			# pop till '(' is found for current ')'
		    while Stack[-1] != '(':
			    Stack.pop()

			# pop '('
		    Stack.pop()

    return False

if __name__ == '__main__':
    # ask user to insert expression
    exp = str(input("Please Enter a expression : "))
    
    # if dup then print dup else not dup
    if Dup(exp):
        print("The expression had duplicate parenthesis.")
    else:
        print("The expression doesn't have duplicate parenthesis.")

