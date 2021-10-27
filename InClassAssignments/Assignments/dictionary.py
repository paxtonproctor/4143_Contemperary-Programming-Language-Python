d1 = dict()

'''
    'python' = 'snake',
    'c++' = 'programming language'
'''

d1['python'] = 'snake'
d1['c++'] = 'programming language'
d1['anaconda'] = 'big snake'
d1['c'] = 'basics'

sList = dict()
stu_list = ['aa', 'bb', 'ff', 'zz', 'bb', 'bb', 'ff', 'cc']

for stu in stu_list:
    if stu in sList:
        sList[stu] += 1
    else:
        sList[stu] = 1

l1 = [1, 3, 4, 7, 8, 5, 2]
target = 13

def sumoftwo(l1, target):
    l2 = [8, 5]
    d1 = dict()

    for i in l1:
        rem = target - i
    if rem in d1:
        return [rem, i]
    else:
        d1[i] = None

print(sumoftwo(l1, target))

print(sList)
sList = {
    'eggs' : 12,
    'pizza' : 2,
    'potato' : 2,
    'python' : 24
}
val = sList.get('python', 0)
print(val)

val = d1.get('anaconda', 0)
print(val)

#d1 = ['python', 'c', 'c++']
if 'python' in d1:
    val = d1['python']
    print('found it', val)
else:
    print('not there')
for key in d1:
    print(key, d1[key])
