sList = dict()
stu_list = ['aa', 'bb', 'ff', 'zz', 'bb', 'bb', 'ff', 'cc']

for stu in stu_list:
    if stu in sList:
        sList[stu] += 1
    else:
        sList[stu] = 1

curr_frequency = 0
for i in sList:
    if curr_frequency < sList[i]:
        curr_frequency = sList[i]
        high_freq = i 
print(high_freq)