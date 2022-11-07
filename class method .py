class Employee:
  var1 = "hi"   # class variable

  def __init__(self):
    self.var2 = "hello"    # Instance variable

  @classmethod             #decorator to define class method
  def any_method(cls):  # need to pass cls as argument, can have more args to this method but cls is mandatory
    print "anything"
    return "hello"

  @classmethod
  def alternative_constructor(cls):
      var4 = "hi"
      return cls #returning object of the class (used to create objects like this)


  @staticmethod        #decorator to define static method
  def stat_method():   #doesn't take cls or self as arg
      print "i am static method"
      print "static method can't access class or instance attributes (var/methods)
      
      


e1 = Employee()

e2 = Employee.alternative_constructor()

print Employee.any_method()  #class method called by class itself
print e1.any_method()        #class method called by object of the class

print e1.stat_method()

print e2    # to tell that it is a object of the class which got created from alternative constructor

print e2.var1   #so this object can access any class variable or method


