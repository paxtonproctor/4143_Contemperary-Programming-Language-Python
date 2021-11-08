 #   lst = ['glenn', 'Sally', 'Joseph']
 #   lst[1] = 'Saikat'
 #   for i in lst:
 #       print(i)
 #   print(lst)

#tp = ('Glenn', 'Sally', 'Joseph')
#c = len(tp)
#print(dir(tp))
#for i in tp:
    #print(i)
#tp[1] = 'Saikat'

text = 'Aruba Jamaica oh I want to take ya Bermuda Bahama come on pretty mama Key Largo Montego baby why dont we go Jamaica Off the Florida Keys theres a place called Kokomo'
words = text.split()
#print(words)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
#print(counts)

lst = []
for key, val in counts.items():
    lst.append((val, key))

nList = sorted(lst, reverse = True)

print(sorted([ (v, k) for k , v in counts.items()]))

for val, key in nList[:10]:
    print(key, val)

tp = ('Saikat', 'Asst', 75)
name, aff, age = tp
print(name, aff, age)

ls = [100010000]

#print(ord('a'))
print(chr(97))

word = 'close'

anagrams = ['locse', 'lcose', 'eoslc', 'closest']
#words = text.split()
#tp_words = tuple(words)
#print(tp_words.count('to'))

#d = {'age': 10, 'classRoll': 7, 'grade': 100, 'gpa': 4}
#lst = []
#for key, val in d.items():
    #lst.append((val, key))
#print(lst)
#newLst = sorted(lst, reverse = True)
#for grade, student in newLst[:3]:
    #print(student, ': ', grade)
#grade, student = newLst[0]
#print(newLst)
#items = d.items()
#print(items)
#i_sor = sorted(items)
#print(i_sor)
#print('items',type(d.items()))
#print('items',type(d.keys()))
#print('items',type(d.values()))

#for key, val in d.items():
    #print(key, val)

#Text = 'From: saikat.das@msutexas.edu\n Here is is'

#for line in text:
    #print(line)