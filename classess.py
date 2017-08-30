class MyClass:
  "This is doc string for MyClass"
  version=1.1

  def __init__(self,num):
    self.num=num
    print "You entered %d and this is Version %f" % (self.num,MyClass.version)

#o=MyClass(3)

class Calculator:
  "This class performs addition and subtraction"
  version=1.1

  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
    print "Welcome to my calculator, version %f" % Calculator.version
  
  def addition(self,num3):
    self.num3=num3
    print self.num3+Calculator.version


#obj=Calculator(23,43)
#obj.num1=100
#obj.version=2000
#obj.addition(13)

#print hasattr(obj,'num1')
#print getattr(obj,'num2')

class Subtractor(Calculator):
  "This class inherits from Calculator"

  def __init__(self):
    print "This is child classes's init"

  def subtract(self):
    print self.num1-self.num2

  def addition(self,num4,num5):
    self.num4=num4
    self.num5=num5
    print self.num4+self.num5

obj=Subtractor()# Here i created child's object
setattr(obj,'num1',343)# But here i edited parent's attribute
setattr(obj,'num2',32)
print getattr(obj,'num1')
print getattr(obj,'num2')

obj.addition(45,66)# Here i have override the parent method




