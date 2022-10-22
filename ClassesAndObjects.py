# class Person:
#   def __init__(self, _name, _age):
#     self.name = _name
#     self.age = _age
   
#   def sayHi(self):
#     print("Hello, my name is" + self.name + " and I am " + self.age + "years old!")
    
# p1 = Person("Bob",str(25))
# p1.sayHi() 

class Employee:
   
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("Zara",str(2000))
emp2 = Employee("Manni",str(5000))
emp1.displayEmployee()
emp2.displayEmployee()


