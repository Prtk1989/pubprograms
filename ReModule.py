# re module

import re

string1 = "heyhihellothere"

sub1 = "hello"

print re.search(sub1,string1)



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