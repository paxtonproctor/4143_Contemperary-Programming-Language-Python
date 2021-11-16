# Paxton Proctor
# Programassignment1
# Problem 1
# CMPS-4143-101 Top: Cont Programming Language
# 10/23/2021
# Make a stack in python using the linked list method

# Class Node
class Node:
    # Constructor initializes node
    def __init__(self,data):
        self.data = data
        self.next = None

# Class Stack
class Stack:
    # Constructor for head
    def __init__(self):
        self.head = None
    

    # add data to the start of the stack
    def push(self, data): 
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    

    #def minimum(self): 
        #if self.min is None:
            #self.min = self.viewtop()
        #else:
            #if self.viewtop() < self.min:
                #self.min = self.viewtop()

    #def Min(self): 
        #return self.min

    #def viewtop(self): 
       # try:
            #return self.data[-1]
        #except IndexError as e:
            #print(e)

    # removes element from start of the stack
    def pop(self): 
        if self.isEmpty():
            print("Stack currently empty")
            return None
        else:
            # puts the new head position to the preceding ele
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            print("popping element successful")
            return poppednode.data            


    #def size(self): 
        #return len(self.data)

    # checks to see if stack is empty
    def isEmpty(self): 
        if self.head == None:
            return True
        else:
            return False

