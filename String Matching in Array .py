#Given an array of string words. Return all strings in words which is substring of another word in any order. 

#String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

#Example 1:

#Input: words = ["mass","as","hero","superhero"]
#Output: ["as","hero"]
#Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
#["hero","as"] is also a valid answer.


class StringMatching():
    def matchsubstring(self,array):
        for i in range(len(array)):
            for item in array:
                if array.index(str(item))!= i:
                    if array[i] in item:
                       print array[i] + " is found as substring in the array"


s = StringMatching()
array= ["mass","as","hero","superhero"]
s.matchsubstring(array)            


#output
#as is found as substring in the array
#hero is found as substring in the array
