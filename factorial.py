while True:
    while True:
        print "Hi! This is factorial program \n"
        try:
         num = input("Enter a number:")
         fact = 1
         if num <0:
          print "Can't calculate the factorial of negative numbers \n"
          break
         elif num ==0:
          print "Factorial of 0 is 1 \n"
          break
         else :
          for i in range(1,num+1):
           fact = fact*i
          print "factorial of", num, "is", fact, "\n"
        except:
                print "Enter integer only \n"
        

#or use in built function

import math
print math.factorial(num)