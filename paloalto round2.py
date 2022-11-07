
import json

f = {}
f = open("/Users/prateekagnihotri/Desktop/file.json",'r+')
dict1 = {}
dict1 = json.load(f)

#print dict1

outdict = {}
print dict1.keys()
valuelist = []
valuedict = {}

for key in dict1.keys():
    valuedict[str(dict1[str(key)])] = dict1[key['containers']]
    valuelist.append(valuedict)

print valuelist

