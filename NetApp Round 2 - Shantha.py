
#1.

#input --> [1,2,3,4]
#output-->[24,12,8,6]


list1 = [1,2,3,4]
list2 = []
def calculate_out(list1):
    list2 = []
    for j in range(0,len(list1)):
        prod = 1
        for i in range(0,len(list1)):
            if j != i:
                prod = prod * list1[i]
        list2.append(prod)
    print list2

calculate_out(list1)


    
#2

#output: a=2,b=2,c=3

string1 = "aabbccc"

def create_count(string1):
    dict1 = {}
    for character in string1:
        count = string1.count(character)
        dict1[str(character)] = count

    print dict1

create_count(string1)

