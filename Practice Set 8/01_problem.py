#Write a program using functions to find greatest of three numbers.
def greatest():
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    c = int(input("Enter your number : "))

    if(a>b and a>c):
        print(f"Greatest number is {a}")
    elif(b>a and b>c):
        print(f"Greatest number is {b}")
    else:
        print(f"Greatest number is {c}")

greatest()

'''
def greatest(a, b, c)
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = 1
b = 23
c = 6

print(greatest(a, b, c))
    '''