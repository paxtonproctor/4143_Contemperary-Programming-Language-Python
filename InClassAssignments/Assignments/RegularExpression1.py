import re

str1 = 'here I am I am I am'
subStr = 'I am'
pos = re.findall(subStr, str1)
print(pos)

slist = ['here I am fhdf I am fkdfjkdf I am', 'I am here', 'I am here']

for s in slist:
    if re.search('^here', s):
    #if s.endswith('am$', s):
    #if s.startswith('here'):
        print(s, '\n')
try:
    hand = open('sample.txt')
    for line in hand:
        if re.search('From:', line):
            print(line)
except:
    print('File not found')

l1 = [11, 11, 11, 11, 11]
print(set(l1))

#with open('sample.txt', 'w') as f: