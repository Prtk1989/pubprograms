print "Dealing with Files"
#Reading from file

targetfile = open("C:\Users\pragniho\Desktop\DDAYDocs\PythonPrograms\prtk.txt", "r+")
print targetfile.readlines() #comes as a list
#print targetfile.read() #reads all lines as string
#print targetfile.readline() #reads first line

#for line in targetfile:
#	print line


#Writing to file and reading in lines

#targetfile = open("prtk.txt", "w+")
#targetfile.write(raw_input("First Line:"))
#targetfile.write("\n")
#targetfile.write(raw_input("Second Line:"))
content = targetfile.readlines()
print type(content)
print content
for x in content:
    print x
#targetfile.truncate() #For erasing data form the file
#targetfile.close()

#Reading from file into dictionary
'''
targetfile = open("prtk.txt", "w+")
d = {}
for line in targetfile:
	x = line.split(" ")
	a = x[0]
	b = x[1]
	b = b[:-1] #for removing \n from the line end
	d[a] = b
print d
'''
