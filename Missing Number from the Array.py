#missing number from the array

#arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
#missing number is 6


def FindMissingNo(array):
    m = len(array)+1 #since 1 number is missing from the list
    actualsum = 0
    sumOfNNatutalNumbers = (m * (m+1))/2
    for i in range(len(array)):
        actualsum = actualsum + array[i]
    missingNum = sumOfNNatutalNumbers - actualsum

    return missingNum

arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print FindMissingNo(arr)


'''
sum of squares of n natural sumOfNNatutalNumbers
n(n+1)(2n+1)/6

'''