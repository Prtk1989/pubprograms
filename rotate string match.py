#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

#A shift on s consists of moving the leftmost character of s to the rightmost position.

#For example, if s = "abcde", then it will be "bcdea" after one shift.
 

#Example 1:

#Input: s = "abcde", goal = "cdeab"
#Output: true

goal = "cdeab"

s = "abcde"

# divide s into 2 parts,goal's 1st character to end in s and s's 1st character to goal's 1st character in s and add them


if s[s.index(str(goal[0])):] + s[:s.index(str(goal[0]))]== goal:
    print "yes its a match"
else :
    print "its not a match"

