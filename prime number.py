import math
while True:
	try :   
		num = int(input("Enter a no:"))
		for i in range(2,int(math.sqrt(num))+1):
			if num%i == 0:  #remainder should not be zero for a number to be prime
				print num, "is not prime"
				break
		else :
			print num, "is prime"

		
	except :
		print "Enter integers only"
