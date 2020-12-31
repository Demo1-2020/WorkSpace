#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     prrint "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
	  
"This would create first object of Employee class"
emp1 = Employee("Zaraa", 2000)
"This would create second object of Employee class"
emp2 = Employee("Mannireddy", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee count %d" % Employee.empCount
