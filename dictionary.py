print "Hi, dealing with dictionary"

dict1 = {'Age':'27', 'Name':'prateek','company':'Oracle'} #while printing it removes duplicate keys if given in dictionary

print dict1, type(dict1)
print str(dict1), type(str(dict1))
print dict1.keys()
print dict1.values()
print dict1.viewkeys()
print dict1.viewvalues()


#output
#{'Age': '27', 'company': 'Oracle', 'Name': 'prateek'} <type 'dict'>
#{'Age': '27', 'company': 'Oracle', 'Name': 'prateek'} <type 'str'>
#['Age', 'company', 'Name']
#['27', 'Oracle', 'prateek']
#dict_keys(['Age', 'company', 'Name'])
#dict_values(['27', 'Oracle', 'prateek'])


'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}
 
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
 
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)



if 'Age' in dict1.keys():
    print dict1['Age'], "hello"
else:
    print "Age is not found in dictionary"

print dict1['Age'], dict1['Name']
del dict1['Age']
print dict1
dict1['Role']= 'Storage QA'
print dict1

dict5 = {}
dict5['a']= 'b'
print dict5


dict2={}
dict2['key1'] = raw_input("Enter the value for key1 in dictionary:")
print dict2

print len(dict2)


#Reading user input in dictionary
dict3 = {}
dict3 = dict3.fromkeys(input("enter key list:"))
for key in dict3.keys():
    dict3[key]= input("enter the value of " + str(key) + ":")
print dict3
print "hello", dict3.items()

#using get

print dict3.get('a', 'a is not a key')
'''
