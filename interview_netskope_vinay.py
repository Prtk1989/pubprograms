

# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!
"""
Problem:
lst = [[1,4,5],[7,8,9],[0,0,1],[100,1,200],[80,-1,0]]
out=

sort using 2nd element
"""
'''
lst = [[1,4,5],[7,8,9],[0,0,1],[100,1,200],[80,-1,0],[0,100,1000]]
list2 = []
for i in range(0,len(lst)):
    list2.append(lst[i][1])

print list2
list3 = sorted(list2)
print list3
list4 = []
for i in list3:
    for item in lst:
        if i == item[1]:
            list4.append(item)

print list4
'''
lst= [[1,4,5],[7,8,9],[0,0,1],[100,1,200],[80,-1,0],[0,100,1000]]
def sort2ndelem(listname):
    list2 = []
    list4 = []
    for i in range(0,len(lst)):
        list2.append(lst[i][1])
    for i in sorted(list2):
        for item in lst:
            if i == item[1]:
                list4.append(item) 

    return list4

print sort2ndelem(lst)

def sort2ndelem2nd(listname):
    list2 = []
    list4 = []
    dict1 = {}
    list3=[]
    for i in range(0,len(lst)):
        dict1[lst[i][1]] = lst[i]

    for key in sorted(dict1.keys()):
        list3.append(dict1[key])

    return list3

sort2ndelem2nd(lst)

"""
Program-2:
Count strings:
    input = [aaa,bbb,123,xyz,netskope]
    strings = {
        "str_1" : "hdhjjdaaakkkkdbbbb"
        "str_2" : "abcda123aaxyznetskopekkkkdbbbbnetskop"
        "str_3" : "etskopehdhjjdaaabbbkkkkdbbbb"
        "str_4" : "aaaabbbxyz123"
    }

    output:
        {"aaa":{"str_1":2,"str_2":1}...
        "bbb":{"str_1":0,"str_2":2}}.... }


    find frequency of comma separated patterns of input-string in strings 1,2,3,4
"""

import re

input = ["aaa","bbb","123","xyz","netskope]
strings = {
        "str_1" : "hdhjjdaaakkkkdbbbb",
        "str_2" : "abcda123aaxyznetskopekkkkdbbbbnetskop",
        "str_3" : "etskopehdhjjdaaabbbkkkkdbbbb",
        "str_4" : "aaaabbbxyz123"
    }


valuedict = {}
outputdict = {}
def findcount(input):
    for item in input:
        for key in strings.keys():
            valuedict[key] = strings[key].count(item)

        outputdict[item] = valuedict
    
    return outputdict

print findcount(input)

