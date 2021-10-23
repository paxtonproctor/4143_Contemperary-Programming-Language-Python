print('Enter some value')
x = input()
print('X val is:', x)

if(int(x)>10 and int(x)<15):
    print('Your entered value is greater than 10')
elif(int(x)>15):
    print('Blah greater than 15 blah')
else:
    print('Your entered value is less than 10')


print('Enter some value')
y =input()
if(int(y) < 20):
    print('blah less than 20')

print('Enter some value')
z = input()
if(int(z) > 5):
    print('less than 5')
else:
    print('greater than 5')


print('end of the program')

try:
    print('I am in Try')
    intVal = int(x)

    while intVal > 0 :
        print(intVal)
        intVal -= 1
except:
    print('You have not entered a numeric value')

k = 1
while(k < 5):
    print('Hello')
    k += 1

l = input()
while (int(l) > 0) :
    m = l + l
    l = l - 1
    print(m)