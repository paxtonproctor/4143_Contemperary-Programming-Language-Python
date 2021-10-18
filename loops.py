import random

def generateRandomValues(n):
    l1 = []
    for i in range(n):
        ranVal = random.randint(100, 200)
        l1.append(ranVal)
    return l1


for i in range(5):
    print(random.randint(1, 10))

l1 = [1, 2, 90, 3, 4, 30]
Largest = None

for i in l1:
    if Largest == None:
        Largest = i
    elif i > Largest:
        Largest = i

l1 = [1, 2, 90, 3, 4, 30]
print(sum(l1))
acc = 0
for val in l1:
    acc+=val
print(acc)
#for i in range(1, 10, 2):
    #print(i)
float('-inf')
l1 = [1, 2, 90, 3, 4, 30]
largest_so_far = float('inf')

for val in l1:
    #largest_so_far = max(val, largest_so_far)
    #if val > largest_so_far:
       #largest_so_far = val
    largest_so_far = min(largest_so_far, val)
print(largest_so_far)

x = input()

try:
    intVal = int(x)
    li = generateRandomValues(intVal)
    for i in l1:
        print(i)

    
    print('length: ', len(l1))
    for val in l1:
        print(val)

    counter = 1
    for val in l1:
        print(counter)
        if val == 30:
            print('I found 30')
            continue
        print(counter,'30 not found')
        counter += 1
    for i in reversed(range(intVal)):
        print(i)
    
    for i in range(intVal):
        print(i)
    

except:
    print('You have not entered a numeric value')