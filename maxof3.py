#!/usr/bin/python
while True:
 print "max of 3 numbers"
 def maxof3():
	 l = []
	 i =1
	 while i < 4:
	  try :
	   l.append(input("enter numbers one by one: "))
	   i = i+1
	  except NameError :
	   print "enter integers only"
	 print l
	 l.sort()
	 print "max of all the 3 numbers is:", l[2]
 maxof3()
 print "================================== \n"


