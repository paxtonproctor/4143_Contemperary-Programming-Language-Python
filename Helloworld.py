#print("Hello world")
var = '3'
#str()convert to string
print(type(var))
var1 = int(var) + 3 # convert to int
print(var1)
#var1 = var + 3
#print(var1)
t1 = int(var)
print(type(t1))

var = '3'
var1 = var*3
print(type(var1))
arr = [0]
arr = arr*3
print(arr)

var = 3
if var < 10:
    print('var is less than 10')
else:
    print('var is greater than 10')
print('end')

var = 31
var1 = var//2
var2 = var/2
var3 = var%5
d, m = divmod(var, 5)
var4 = 2**3
float('-inf')
print(float('-inf'))
print(var4)
print(d, m)
print(var1, var2, var3)

var1 = 'Hello'
var2 = ' World!'
print(var1 + var2)

# input lets the user type something
print('Enter your first and last name')
var5 = input()
var6 = input()
print(var5)
print('Your name is: ', var5, var6)