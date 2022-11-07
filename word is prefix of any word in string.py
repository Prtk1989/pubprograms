#Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

#Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
#If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
#If there is no such word return -1



sentence1 = "this is a python program"
sentence2 = "this is a python program out of many programs"
word = "pro"
list2=[]

def findprefixword(sentence,word):
    list1 = sentence.split(" ")
    for item in list1:
        if item.startswith(word):
            list2.append(list1.index(item)+1)

    print list2[0]

findprefixword(sentence2,word)



