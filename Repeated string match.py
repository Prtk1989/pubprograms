#Input: a = "abcd", b = "cdabcdab"
#Output: 3
#Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.


a = "abcd"
b = "cdabcdab"


for i in range(1,len(b)):
    if b in a*i:
        print "repeat the string" , i , " times then you will find it. "
        break
