

import copy

list1 = [1,4,2,5]
list2 = [6,3,[2,4],44]

list3 = copy.deepcopy(list1)

print list3
print id(list3)

list4 = copy.copy(list2)

print list4
print id(list4)
print id(list1)
print id(list2)

list2[2][0] = 45
#if you change any element in original list then it will appear in shallow copy also
#if you insert any new element in original list then it will not appear in shallow copy

print list2
print id(list2)    #id of list2 will remain same as original even after changing element
print list4


