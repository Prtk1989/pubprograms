#!/usr/bin/python
while True:
 def is_member(a,x):
  for l in range(0,len(x)):
   if x[l] == a[0] :
    print a[0], "is in the list"
    break
   else :
    print a[0], "isn't in the list"
   break
 a = []
 a.append(raw_input("Enter a character:"))
 x = []
 i = 1
 while i < 5 :
  x.append(raw_input("Enter the list items one by one:"))
  i = i+1
 is_member(a,x)
