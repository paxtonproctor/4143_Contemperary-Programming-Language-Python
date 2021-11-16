class stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        if len(self.stack)!=0:
            return True
        return False

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.empty():
            return self.stack.pop()

    def print_s(self):
        return self.stack

st = stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
stack = [0, 4, 5]
stack.append(1)
print(stack)

#push()
stack.append(2)
print(stack)

#top()
print(stack[-1])
print(stack)

#pop()
print('Popped',stack.pop())
print(stack)

#size()
print('size',len(stack))

#empty()
