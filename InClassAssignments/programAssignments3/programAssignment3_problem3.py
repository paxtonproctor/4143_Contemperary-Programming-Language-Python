# Paxton Proctor
# Programassignment3
# Problem 3
# CMPS-4143-101 Top: Cont Programming Language
# 11/16/2021
# Find the Avg of a stream numbers using a stack or queue in python

class AverageStream:
    # constructor to get int size of numbers
    def __init__(self, size: int):
        self.numbers = []
        self.size = size
        
    # next takes the element turns it into a float
    # adds a value to the end of the list
    def next(self, val: int) -> float:
        self.numbers.append(val)
        if len(self.numbers) > self.size:
            return sum(self.numbers[-(self.size):]) / self.size
                
        return sum(self.numbers) / len(self.numbers) 

stack = []

# Insert the size of the window.

inputSize = int(input("Please Enter a Window Size: "))
streamElement = int(input("Enter the 1st ele: "))
streamElement2 = int(input("Enter the 2st ele: "))
streamElement3 = int(input("Enter the 3st ele: "))
streamElement4 = int(input("Enter the 4st ele: "))

obj = AverageStream(inputSize)

# Adding elements to the Empty stack.
res = obj.next(streamElement)
stack.append(res)

res = obj.next(streamElement2)
stack.append(res)

res = obj.next(streamElement3)
stack.append(round(res,2))

res = obj.next(streamElement4)
stack.append(res)
print(stack)


# Removing elements from the stack

stack.pop(0)
stack.pop(0)
stack.pop(0)
stack.pop(0)


# Changing the window size then adding elements to the Empty stack.

inputSize2 = int(input("Please Enter a Window Size: "))
streamEle = int(input("Enter the 1st ele: "))
streamEle2 = int(input("Enter the 2st ele: "))
streamEle3 = int(input("Enter the 3st ele: "))
streamEle4 = int(input("Enter the 4st ele: "))

obj = AverageStream(inputSize2)
res = obj.next(streamEle)
stack.append(res)

res = obj.next(streamEle2)
stack.append(res)

res = obj.next(streamEle3)
stack.append(round(res,2))

res = obj.next(streamEle4)
stack.append(res)
<<<<<<< HEAD
print(stack)
=======
print(stack)
>>>>>>> e09460efc4d48070aba51e851a85ab3729671b70
