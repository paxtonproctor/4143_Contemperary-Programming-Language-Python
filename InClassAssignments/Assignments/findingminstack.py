class Stack(): 
    def __init__(self):
        self.data = [] 
        self.min = None

    def push(self, item): 
        self.data.append(item)
        self.minimum()

    def minimum(self): 
        if self.min is None:
            self.min = self.viewtop()
        else:
            if self.viewtop() < self.min:
                self.min = self.viewtop()

    def Min(self): 
        return self.min

    def viewtop(self): 
        try:
            return self.data[-1]
        except IndexError as e:
            print(e)

    def pop(self): 
        if self.isEmpty():
            print("Stack currently empty")
        else:
            print("popping element successful")
            return self.data.pop()

    def size(self): 
        return len(self.data)

    def isEmpty(self): 
        return self.size() == 0


stack = Stack() 
stack.push(1)
stack.push(-50)
stack.push(500)
stack.push(12)
print(" THe min value in our stack is : ", stack.Min())
stack.push(-37)
stack.pop()
stack.push(-43)
print(" THe min value in our stack is : ", stack.Min())