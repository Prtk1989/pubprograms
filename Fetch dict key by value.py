

dict1 = {'stu1':'prateek','stu2':10}

val = 10   #value for which key needds to be found

indexOf10 = dict1.values().index(val)

print dict1.keys()[indexOf10]


print dict1.keys()[dict1.values().index(val)]



