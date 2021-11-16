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
        self.min = None
    

    # add data to the start of the stack
    def push(self, data): 
        if self.head == None:
            self.head = Node(data)
            print("Successfully pushed: ", self.head.data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            print("Successfully pushed: ", self.head.data)
        self.minimum()
    
    # tracks minimum value
    def minimum(self): 
        if self.min is None:
            self.min = self.top()
        else:
            if self.top() < self.min:
                self.min = self.top()

    # gets minimum
    def Min(self): 
        return self.min

    # tries to check if top is empty else point to data
    def top(self): 
        try:
            if self.isEmpty():
                return None
            else:
                return self.head.data
        except IndexError as e:
            print(e)

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
            print("popping element successful: ", poppednode.data)
            return poppednode.data            

    # gets the Size of the stack
    def size(self): 
        iterateNode = self.head
        if self.isEmpty():
            print("Stack is empty")
        else:
            while(iterateNode != None):
                print(iterateNode.data,"->", end = " ")
                iterateNode = iterateNode.next
            return
        

    # checks to see if stack is empty
    def isEmpty(self): 
        if self.head == None:
            return True
        else:
            return False

NodeStack = Stack()

NodeStack.push(12)
NodeStack.push(13)
NodeStack.push(18)
NodeStack.push(23)
NodeStack.push(43)
NodeStack.push(34)

NodeStack.size()

print("\nTop of Stack is:", NodeStack.top())

NodeStack.pop()
NodeStack.pop()
NodeStack.pop()

print("here is the minimum after push: ",NodeStack.Min())

print("Top of Stack is:", NodeStack.top())

NodeStack.push(3)

NodeStack.size()

print("\nhere is the new minimum after push: ",NodeStack.Min())