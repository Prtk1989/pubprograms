#!/usr/bin/python
print "This is file handling exercise"
fo = open('/Users/prateekagnihotri/Desktop/PythonPrograms/sample1.txt', 'r+')
print "Name of the file is:", fo.name
print fo.name,"is opened in", fo.mode, "mode"
print "file got closed: ", fo.closed
print fo.read(7)

fo.write("eeeeeeeeeeeeeee")
#for lines in fo:
# l = lines.split()
# print l[0]
# print l[1]
print fo.read()
fo.close()
print "file got closed: ", fo.closed
