'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?''' # Ans - No

class Demo:
    a = 4

o = Demo()
print(o.a) # prints class attribute bcoz instance attribute is not present
o.a = 0 # instance attribute is set
print(o.a) #prints instance attribute bcoz instance attribute is present
print(Demo.a) # prints the class attribute