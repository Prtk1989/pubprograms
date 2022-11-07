print "Hi!! This is your calculator"
while True:
        try :
            while True:
                 num1 = input("Enter the first number:")
                 operator = raw_input("Enter the operation you want to perform(+,-,*,**,/,%), q to exit the program:")
                 if operator =="q" or operator =="Q":
                  break
                 else :
                    num2 = input("Enter the second number:")
                    if operator == "+":
                        print "Answer for", num1,operator,num2, "is", num1+num2
                        print "\n"
                    elif operator == "-":
                        print "Answer for", num1,operator,num2, "is", num1-num2
                        print "\n"
                    elif operator == "*":
                        print "Answer for", num1,operator,num2, "is", num1*num2
                        print "\n"
                    elif operator == "/":
                        print "Answer for", num1,operator,num2, "is", num1/num2
                        print "\n"
                    elif operator == "%":
                        print "Answer for", num1,operator,num2, "is", num1%num2
                        print "\n"
                    elif operator == "**":
                        print "Answer for", num1,operator,num2, "is", num1**num2
                        print "\n"
                    else :
                        print "you have not entered the correct operator!\n"
                        False 
        except :
            print "kindly enter integers only\n"
