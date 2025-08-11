'''
factorial(0) = 0
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1
factorial(n) = n * n-1 * ...... 3 * 2 * 1

factorail(n) = n * factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f"The factorial of {n} is {factorial(n)}")