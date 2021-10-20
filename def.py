

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print('Give me nth fib number')
z = input()
z = int(z)
fibn = fib(z)
print(fibn)

print('Enter two values')
x, y = input().split()
print('You have entered:', x , y)

def addition(par1, par2):
    return par1 + par2

try:
    x = int(x)
    y = int(y)

    res = addition(x, y)

    print(res)
except:
    print('You have not entered a numeric value')

print('Enter Hours and Rate')
a, b, c = input().split()
print('You have entered:', a , b, c)

def computepay(par1, par2, ot):
    return ((par1 * par2) + (ot * (par2 / 2)))

try:
    a = int(a)
    b = int(b)
    c = int(c)
    res = computepay(a, b, c)
    print('Pay: ', res)
except:
    print('You have not entered a numeric value')

str1 = '   apple'
#str2 = str1[3:]
str2 =str1.lstrip()
#str2 = str2 + str1[1] + str1[2]
print(str2)
