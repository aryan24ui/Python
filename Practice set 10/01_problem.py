#Create a class “Programmer” for storing information of few programmers working at Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

name = input("Enter your name : ")
salary = int(input("Enter your salary : "))
pin = int(input("Enter your pin code : " ))
p = Programmer(name, salary, pin)
print(p.name, p.salary, p.pin, p.company)

#r = Programmer("Rohan", 1200000, 206001)
#print(r.name, r.salary, r.pin, r.company)