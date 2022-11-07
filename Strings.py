print "Hi!, dealing with strings"
str1 = "HiHelloByeChallo9"
print str1[:3] + 'yoyo'
print str1.count("h")
print str1.find("k")   #returns the index where "k" is found
#print str1.index("ch")   #return the index where "ch" is found otherwise raises error if "ch" is not found
print str1.count(" ")
print str1[3:]
print str1[-3:]
print str1[:-3]
print str1[-3:-3]
print str1[:]
print str1.startswith("h")
print str1.endswith("h")
st = str1.split("i",1) #can give count how many times to split a string based on this character
print st[0]
print st[1]
print type(st)
print str1.replace("hi","heylo")
print str1.upper()
print str1.lower()
print str1.swapcase()
print str1[::-1]
print str1[::-2]

print str1.isupper()
print str1.islower()
print str1.isspace()
print str1.isalnum()

s = 'a123b'

for char in s:
    print(char, char.isalpha())

    