#Write a python program using function to convert Celsius to Fahrenheit.
def temp():
    t = int(input("Enter the temperature in Celsius : "))
    F = ((9/5) * t) + 32
    return F

print(f"Temperature in Fahrenheit is {temp()}")