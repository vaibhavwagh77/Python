class Programmer:
     company= "microsoft"
     sex = "male"
     def __init__(self, name, salary, pin):
          self.name = name
          self.salary = salary
          self.pin = pin

p = Programmer("vaibhav", 120000, 422101,)
emp1=(p.name, p.sex,p.salary, p.pin, p.company)
print(emp1)

 