class queue:
  def __init__(self):
    self.q = []
  
  def enqueue(self, data):
    self.q.append(data)

  def dequeue(self):
    self.q.pop(0)

  def rear(self):
    if self.q:
      return self.q[-1]
    
  def front(self):
    if self.q:
      return self.q[0]

q1 = queue()
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1.q)
q1.dequeue()
print(q1.q)


def isValid(str1):
  stack = []
  for ch in str1:
    if ch == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        return False

    elif ch == '}':
      if stack and stack[-1] == '{':
        stack.pop()
      else:
        return False
    elif ch == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        return False
    else:
      stack.append(ch)

  if len(stack)!=0:
    return False
  else:
    return True
