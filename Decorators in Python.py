# Decorators in Python



def Decorator_Func(function_as_arg):

    def InnerFunc():
        print "I am Inner function, going to execute function passed as arg in Decorator Function"

        function_as_arg()

        print "decorator function executed, tata"
        
    return InnerFunc


@Decorator_Func
def function1():
    print "I am argument function"


function1()

#output
'''
I am Inner function, going to execute function passed as arg in Decorator Function
I am argument function
decorator function executed, tata
