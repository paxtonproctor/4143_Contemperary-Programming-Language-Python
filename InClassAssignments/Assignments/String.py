s1 = 'I am good'
s2 = 'abd'
l1 = [100, 20, 303, 4]
l2 = ['saikat', 'das', 'msu']
l3 = [10, 20, 30, 'saikat', ['saikat', 'das', 'msu']]
l2.sort()
print(l2)
l1.sort()
print(l1)
stuff = s1.split()
print(stuff)
#l5 = []
#for idx in range(len(l1)):
    #newval = l1[idx] + l2[idx]
    #print(l5)
    #l5.append(newval)
    #print(newval)
l6 = [0 for _ in range(len(l1))]
for idx in range(len(l1)):
    l6.append(0)
l4 = l1 + l2
print(l4)
print(l3[4][2])

for idx in range(len(l3)):
    print(l3[idx])

for val in l3:
    print(val)

for val in l3:
    print(val)

for idx, val in enumerate(l3):
    print(idx, val)

s1 = s1.replace('good', 'bad')
print(s1)
l1[2] = 50
print(l1)

s3 = '10 with words'
for ch in s3:
    print(ch, ch.isnumeric())
print(s3.isnumeric())
print(s3.endswith('1words'))

print(s1.find('am'))
if 'am1' in s1:
    print('I found it')

if(s2.islower()):
    print('s2 is lower cased')

if s1 == s2:
    print('Equal')
elif s2 > s1:
    print('s2 is bigger')
elif s2 < s1:
    print('s1 is bigger')

for idx in range(len(s1)):
    print(s1[idx])

for ch in s1:
    print(ch)


print(s1)
print('g' in s1)


print(50 in l1)
