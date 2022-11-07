
'''
1. 

string1 = "abc1de2f"

output = "fed1cb2a"
outstring = ""
list1 = []
dict1 = {}
for i in range(len(string1)-1,-1,-1):
    if string1[i].isalpha():
        list1.append(string1[i])
    else :
        dict1[str(string1[i])] = i
        
    
list2 = dict1.keys()
list3 = dict1.values()

for i in range(0,len(list2)):
    list1.insert(list3[i],list2[i])


print "".join(list1)
        

2. implement tail with grep in python
'''

inputstring = "bye"

f = open("/Users/prateekagnihotri/Desktop/PythonPrograms/prtk.txt",'r+')

a = f.readlines()

for line in a :
    if inputstring in line:
        print line
