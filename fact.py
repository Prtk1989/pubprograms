print "factorial program"

num = input("Enter the number for which you want to calculate the factorial:")

def factorial(num):
	fact = 1
	if num < 0:
		print "Can't calculate the factorial for negative numbers."
	else :
		for i in xrange(1, num +1):
			fact = fact * i
		print "factorial of", num, "is", fact
		
factorial(num)
			