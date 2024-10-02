
class Emp:
    lang = "python"
    sal = 70000

    def __init__(self): #dunder method
        
        print("making an object")

    def getinfo(self):
        print(f"the lang is {self.lang} and salary is {self.sal}")
    @staticmethod
    def greet():
        print("hello boy/girl")

vaibhav = Emp()
vaibhav.name = input("Enter the name: ")
print(vaibhav.name)
vaibhav.getinfo()
vaibhav.greet()