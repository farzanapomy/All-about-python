class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, increase=1000):
        self.salary += increase


# 1. Write a Python Class named ‘Employee’ and show its type. Also show the __dict__ attributes and the values of __module__ attribute of that class.
emp1 = Employee("John", 25, 1000)
print(type(emp1))
print(emp1.__dict__)
print(emp1.__module__)
 