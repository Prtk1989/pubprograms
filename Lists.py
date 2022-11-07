
li = []
print "Hi!, dealing with lists"

#remove duplicates from the list
#############################

my_list = ['a','x','a','y','a','b','b','c']
my_final_list = dict.fromkeys(my_list) #to remove duplicate items from list
print list(my_final_list)

#using list comprehension
my_list = [1,2,2,3,1,4,5,1,2,6]
my_finallist = []
[my_finallist.append(n) for n in my_list if n not in my_finallist] 
print my_finallist

#using set
my_list = [1,1,2,3,2,2,4,5,6,2,1]
my_final_list = set(my_list)
print list(my_final_list)

#using ordered dict
from collections import OrderedDict

my_list = ['a','x','a','y','a','b','b','c']

my_final_list = OrderedDict.fromkeys(my_list)

print list(my_final_list)
###############################

list1 = [-4,-21,-2,-45,-12,34,4,12,3,-23,-34,-34,-34]

print sorted(list1)  #sorts list with both positive and negative numbers

list1.sort()
print list1


#zip
list1 = [[1,2,3],[4,5,6],[7,8,9]]

print zip(*list1[::-1])   #[(7, 4, 1), (8, 5, 2), (9, 6, 3)]

print zip(*list1[:])   #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]



#remove works on element name itself
my_list = [12, 'Siya', 'Tiya', 14, 'Riya', 12, 'Riya']
my_list.remove('Riya')  # 1st matching Riya will be removed

#pop function to remove element, this works on index
my_list = [12, 'Siya', 'Tiya', 14, 'Riya', 12, 'Riya']

#By passing index as 2 to remove Tiya
name = my_list.pop(2)
print(name)
print(my_list)

#pop() method without index – returns the last element
item = my_list.pop()
print(item)
print(my_list)

#passing index out of range, thorws error
item = my_list.pop(15)
print(item)
print(my_list)

#my_list.clear() will delete all the list

#del deletes with indexes and slicing as well

del my_list[2:4]
print my_list



list1 = [4,2,56,3,4,5]

list1.reverse()   #reverses the string but doesn't print anything if you try to print, print list in next line to see

print list1

# input list
lst = [10, 11, 12, 13, 14, 15]
l = []  # empty list
 
# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)

list1.sort()  # sorts the list but doesn't print anything if you try to print, print list in next line to see

print list1


#print all the indexes of a string in a list
my_list = ['Guru', 'Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 
print("Originallist ", my_list)
all_indexes = [a for a in range(len(my_list)) if my_list[a] == 'Guru']
print("Indexes for element Guru : ", all_indexes)

li = input("enter list:")
print li, type(li)
list1 = ['hi',14,15,"heo"]
print list1
print list1[2]
#list1[4]= 13
#print list1
list1.append(13)
print list1
print max(list1)
print min(list1)
print list1.count(14)
list2 = [123,245]
list1.extend(list2)
print list1
list2.insert(2,2345)
print list2
print list1.index(13)
print list1.count(13)
list1.sort()
list1.sort(reverse = True)

print list1.copy()
#see copy function of list --- it does shallow copy of the list, means any changes to new copied list won't be permanent to old list

pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)
>>> pow2 = [2 ** x for x in range(10) if x > 5]
>>> pow2
[64, 128, 256, 512]
>>> odd = [x for x in range(20) if x % 2 == 1]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#imp
>>> [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
['Python Language', 'Python Programming', 'C Language', 'C Programming']