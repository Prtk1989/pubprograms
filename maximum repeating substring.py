class Solution(object):
    def maxRepeating(self, sequence, word):
        
        if word in sequence :
            count = sequence.count(str(word))
            return count
        else:
            print "the word is not there in the sequence"
            
s = Solution()
sequence = "ababc"
word = "ab"
print "count is " , s.maxRepeating(sequence,word)
