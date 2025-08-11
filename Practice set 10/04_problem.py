#Add a static method in problem 2, to greet the user with hello.
class Calculator:

    @staticmethod
    def greet():
        print("Hello User!")
    
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")

    def square_root(self):
        print(f"The square root of {self.n} is {self.n**1/2}")

num = int(input("Enter the number : "))
calc = Calculator(num)

calc.greet()
calc.square()
calc.cube()
calc.square_root()
