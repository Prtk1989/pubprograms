
#1. Program to find a pair in the array (all +ve numbers) whose sum is equal to a number

def findnum(arr,x):
    i = 0
    j = len(arr)-1

    while i < j :
        if arr[i]+arr[j] == x:
            print "the pair is: " + str(arr [i]) + " and " + str(arr[j])
            return 1
        elif arr[i]+ arr[j] < x:
            i = i + 1
        else:
            j = j - 1
            
arr= [1,2,4,5,12,34,76]
findnum(arr,16)
#complexity - O(n)

#2 Program to find a pair in the array (+ve and -ve numbers) whose sum is equal to a number

def findnum1(arr1,x):
    i = 0
    j = len(arr1)-1

    while i < j :
        if arr1[i]+arr1[j] == x:
            print "the pair is: " + str(arr1 [i]) + " and " + str(arr1[j])
            return 1
        elif arr1[i]+ arr1[j] < x:
            i = i + 1
        else:
            j = j - 1
            
array1= [1,2,4,5,12,34,76,-1,-2]
arr1 = array1.sort()

findnum1(arr1,16)

#same programs can be done with n**2 complexity with 2 for: loops

def findnum2(array,x):
    i =0
    j = len(array)
    for i in range(0,j):
        for j in range(i+1,j):
            if array[i] + array[j] == x:
                print "match found"
                return 1

arr= [1,2,4,5,12,34,76]
findnum2(arr,16)

#3. program to find all the pairs in the array whose sum is less than a number

array1 = [1,2,4,5,12,34,76,-1,-2]

#sort method doesn't work on a list with positive and negative numbers both
#for that prepare 2 lists with positive and negavtive numbers separately
#and then sort these 2 list and concatenate so you will get a final list with sorted numbers

array = [1,2,4,5,12,34,76]
x = 10
def findpair(array,x):
    i = 0
    j = len(array) -1
    a = []
    while i < j :
        
        if (array[i]+ array[j] < x):
            a.append((array[i],array[j]))
            i = i+1
        else:
            j = j -1
    for i in range (0,j):
        if (array[i]+array[i+1] < x ):
            a.append((array[i],array[i+1]))
            i = i +1

    print list(set(a))

findpair(array,x)

         
#4. calculate time taken to run the function

import timeit
t = timeit.Timer(lambda :findpair(array,x))
print t.timeit(1)
