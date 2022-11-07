#All sublists of a list


def SublistArray(array):
    finalList=[]
    for i in range(len(array)+1):
        for j in range(i+1,len(array)+1):
            if array[i:j] not in finalList:
                finalList.append(array[i:j])
    return finalList


array = [3,4,65,12,34,67]
print (SublistArray(array))

