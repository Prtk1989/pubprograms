import re
import sys
string1 = raw_input("Enter any string:")

for key in "".join(set(string1)):
 #print "".join(set(string1))   # set(string1) removes duplicates & gives a list of individual characters and "".join gives a string of that list without spaces
 sys.stdout.write(key,string1.count(key))

#to find overlapping matches

#print [m.start() for m in re.finditer('(?=tt)', 'ttt')]



import re
print [m.start() for m in re.finditer('(?=ab)', 'sdsxabefdzsvabdfsvabsdvsab')]

#output [4, 12, 18, 24]



#print key,string1.count(key)



print re.split(r'\s',string1)   #split the string at spaces
print re.split(r's',string1)   #split the string at character 's'
string1.split('s') #split the string at character s and give a list


import re
string1="shdvnjksfhxcjdks"


print re.split(r'\s',string1)   #split the string at spaces
print re.split(r's',string1)   #split the string at character 's' and give a list
print string1.split('s')       #split the string at character s and give a list

#output 
#['shdvnjksfhxcjdks']
#['', 'hdvnjk', 'fhxcjdk', '']
#['', 'hdvnjk', 'fhxcjdk', '']



import re
print re.search("abc","sfhz hBJabcdnfhjabc") #gives a match object if substring exists in the string else gives None
#so if re.search("abc","sfhz hBJabcdnfhjabc"): #means if its true
#      print "substring is found"