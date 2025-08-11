#Write a python function which converts inches to cms
def cms():
    inches = int(input("Enter the number in inches : "))
    I = inches * 2.54
    return I

print(f"Number in cms is {cms()}")