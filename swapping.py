while True:
 try :
     print "\nHi!, this is swapping program \n"
     x = input("Enter the value of x:")
     y = input("Enter the value of y:")
     #x,y = y,x
     x = x+y
     y= x-y
     x= x-y
     print "after swapping, the value of x is", x
     print "after swapping, the value of y is", y
 except :
     print "Enter numeric values only"
