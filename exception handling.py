try:
    a = 10
    b = 0

    print a / b

except Exception as e :
    print e.message    #prints error message
    #raise e    #raises error and halts the program
    #raise ValueError



import math


def num_stats(x):
    if x is not int:
        raise TypeError('Work with Numbers Only')
    if x < 0:
        raise ValueError('Work with Positive Numbers Only')

    print(f'{x} square is {x * x}')
    print(f'{x} square root is {math.sqrt(x)}')



try:
    	while True:
       		 #input is assigned to a string variable check
        		check = raw_input('The input provided by the user is being read which is:')
        		#the data assigned to the string variable is read
        		print 'READ:', check
#EOFError exception is caught and the appropriate message is displayed
except EOFError as x:
   	 print x
   	 #pass    can pass also
