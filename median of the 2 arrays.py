#find the median of the 2 sorted arrays (if needed, then sort them)
#merge the arrays and find the middle element if odd or avg of middle 2 elements if even nos


list1 = [23,1,4,2,4,5,-2,-4,-5,-78]  #even nos

#list2 = [-2,-3,-4,11,12,56,34,23,78,98,-1]   #odd nos

list2 = [-2,-3,-4,11,12,56,34,23,78,-1]  #even nos , take list1 and this list2 for 2 even lists


list3 = sorted(list1+list2)

if len(list3)%2 == 0:
    print "there are even nos in the merged list"
    print "find middle 2 elements of the list"
    n = len(list3)/2
    print "middle 2 elements are : " , list3[n-1],  list3[n]
    print "median of the list is : ", (list3[n-1]+list3[n])/2

else:
    print "there are odd nos in the merged list"
    print "find middle element of the list"

    print "middle element and median of the list is : " , list3[len(list3)/2]


#output
#RESTART: /Users/prateekagnihotri/Desktop/PythonPrograms/median of the 2 arrays.py 
#there are odd nos in the merged list
#find middle element of the list
#middle element and median of the list is :  4
#>>> 
# RESTART: /Users/prateekagnihotri/Desktop/PythonPrograms/median of the 2 arrays.py 
#there are even nos in the merged list
#find middle 2 elements of the list
#middle 2 elements are :  2 4
#median of the list is :  3
