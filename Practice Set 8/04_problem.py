#Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + sum(n-1)
    
n = int(input("enter the number : "))

print(f"The sum of first {n} natural number is {sum(n)}")