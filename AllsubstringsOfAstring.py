#all substrings of a string


string1 = "abab"
list1= []
for i in range(len(string1)+1):
    for j in range(i+1,len(string1)+1):
        if string1[i:j] not in list1:
            list1.append(string1[i:j])

print (list1)

'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

'''

'''
for item in list1:
    for i in range(1,len(string1)):
        if item*i == string1:
            print ("yes the string '",string1, "' can be made after" ,i, "iterations of adding '", item, "'")
            break
'''