#Encapsulation in Python

#Private and protected members

Encapsulation in Python describes the concept of bundling data and methods
within a single unit. So, for example, when you create a class, it means you
are implementing encapsulation. A class is an example of encapsulation as
it binds all the data members (instance variables) and methods into a single
unit.


Encapsulation can be achieved by declaring the data members and methods of a
class either as private or protected. But In Python, we don’t have direct
access modifiers like public, private, and protected. We can achieve this
by using single underscore and double underscores.

Access modifiers limit access to the variables and methods of a class.
Python provides three types of access modifiers private, public, and protected.


Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class
Protected Member: Accessible within the class and its sub-classes
Data hiding using access access modifiers


class Employee:
    def __init__(self,name,salary):
        self.name = name -------> Public member (accessible outside the class)

        self._project = project ----> Protected member (accessible within class and subclasses)

        self.__salary = salary ------> Private member (accessible within class only)



#try to access private member which throws error

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp.__salary)

Output : AttributeError: 'Employee' object has no attribute '__salary'


But private members can be accessed outside using
1. public method of the class
2. Name mangling

########## using Public method
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()

########   using Name Mangling

The name mangling is created on an identifier by adding two leading underscores
and one trailing underscore, like this _classname__dataMember, where classname
is the current class, and data member is the private variable name.


class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)




