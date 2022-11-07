#Find the longest substring without repeating characters



#string1= "whfabsjdfkvhfvhakcnvbahlkdvsbalhjcbvslh"

string1 = "vbhvbhdjnsadufjsdhvsfshjvfdhdfbvdsbvjgsdzkb"
list1 = []

for i in range(len(string1)):
    if string1[i] not in list1:
        list1.append(string1[i])
print str(list1)

string2 = ''.join(list1)    #joined elements of a list into a string
print string2

for j in range(len(string2),0,-1):
    if string2 in string1 :
        string3 = string2

    else :
        string2 = string2[:-1]

print "longest substring is : " , string3

'''
using function

def check(string1):
    list1 = []
    for i in range(len(string1)):
        if string1[i] not in list1:
            list1.append(string1[i])

    string2 = ''.join(list1)    #joined elements of a list into a string
    
    for j in range(len(string2),0,-1):   #read in reverse
        if string2 in string1 :      
            string3 = string2

        else :
            string2 = string2[:-1]   #keep reducing 1-1 chracters from the right to check substring in string
            
    return string3

check(string1)

'''
'''
#outputs
1.
['w', 'h', 'f', 'a', 'b', 's', 'j', 'd', 'k', 'v', 'c', 'n', 'l']
whfabsjdkvcnl
longest substring is :  whfabsjd

2. 

['v', 'b', 'h', 'd', 'j', 'n', 's', 'a', 'u', 'f', 'g', 'z', 'k']
vbhdjnsaufgzk
longest substring is :  vbhdjnsa
>>> 
'''
        
    

