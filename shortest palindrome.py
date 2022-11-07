'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"

revs = "aaacecaa"
Output: "aaacecaaa"

'''

s = "abcd"
revs = s[::-1]
substringarray = []

def palindrome_check(string):
    if string == string[::-1]:
        return True

for i in range(0,len(revs)):
    for j in range(i+1,len(revs)+1):
        if revs[i:j] not in substringarray:
            substringarray.append(revs[i:j])

for item in substringarray:
    string = item + s
    if palindrome_check(string):
        print item , "is the string that you need to add at the front to make it palindrome"
        break
    
        
