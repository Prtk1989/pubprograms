
class Person:
  def __init__(self, name, age):  
  #init is used as It's a object constructor that define default values upon calling the class. 
  #This method called when an object is created from the class 
  #and it allow the class to initialize the attributes of a class.
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class PersonAgain(Person):
  pass

p2 = PersonAgain("prateek",33)

print p2.name
print p2.age

#2 Python program to illustrate destructor
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
del obj


#destrcutor is called when the object is deleted, not used much in python as python as in built GC

The child's __init__() function overrides the inheritance of the parent's __init__() function.

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


#3 Class variable is defined inside class but outside any method

class Employee:
  var1 = "hi"   # class variable

  def __init__(self):
    self.var2 = "hello"    # Instance variable

  @classmethod             #decorator to define class method
  def any_method(cls):     # need to pass cls as argument, can have more args to this method but cls is mandatory
    print "anything"

e1 = Employee()

print Employee.any_method()
print e1.any_method()






    