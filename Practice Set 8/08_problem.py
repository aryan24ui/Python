#Write a python function to print multiplication table of a given number.
'''
def print_table(number, multiplier=1):
    if multiplier > 10:
        return
    print(f"{number} x {multiplier} = {number * multiplier}")
    print_table(number, multiplier + 1)

num = int(input("Enter a number: "))
print_table(num)'''

def multiply():
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter the number : "))
print(multiply())
