

#1. import re


#2. reverse a string
'''
string1 = "prateek"

print string1[::-1]

#or
string2 = ""

for i in range(len(string1)-1,-1,-1):
    string2 = string2 + string1[i]
print string2
    

#or
string2 = ""
for i in string1:
    
        string2 = i + string2
        print string2
        
    

print string2
'''

#3 Remove duplicates in list

list1 = [1,1,2,2,3,3]
list2 = [1,2,3,1,2,3,1,2,3]

#print list(set(list1))

list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)

print list2

#or
dict1 = dict.fromkeys(list2)
print dict1


#or
list4 = []
[list4.append(n) for n in list1 if n not in list4]
print list4



#or
list2 = [1,2,3,1,2,3,1,2,3]
for item in list2:
    if list2.count(item) > 1:
        list2.pop(list2.index(item))
print list2

#4  constructor class



