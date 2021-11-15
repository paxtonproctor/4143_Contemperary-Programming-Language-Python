# Paxton Proctor
# Programassignment2
# Problem 2
# CMPS-4143-101 Top: Cont Programming Language
# 11/8/2021
# (35 points) Given an array of strings strs, group the anagrams together. You can return the
# answer in any order.

stu = []
stu = [item for item in input("type in your inputs: ").split()]

# Anagram
def AnagramKey(string):
    # gets each string and sorts it
    key = ''
    for ch in sorted(string):
        key += ch
    return str(key)
 
# gets the strings and groups them using a dictionary and
# for each ele you compare to another then append it and return the group
def AnagramWords(stu):
    group = dict()
    for ele in stu:
        if group.get(AnagramKey(ele)) == None:
            group[AnagramKey(ele)] = [ele]
        else:
            group[AnagramKey(ele)].append(ele)
    return group
 
 
anagram_grouped = AnagramWords(stu)
# Anagram in dictonry format
print(anagram_grouped)

anagram_grouped_list = list()

for k, v in anagram_grouped.items():
    anagram_grouped_list.append(v)
print('In list format')
print(anagram_grouped_list)