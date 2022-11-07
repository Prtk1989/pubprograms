while True:
	print "Hi!,This is palindrome program \n"
	str = raw_input("Enter the string:")
	#if list(str) == list(reversed(str)):
        #        print "the string is palindrome \n"
        #else :
        #        print "The string is not palindrome \n"
 
	if str == str[::-1]:
		print "string is palindrome."
	else:
		print "not palindrome"
