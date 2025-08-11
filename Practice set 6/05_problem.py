#Write a program which finds out whether a given name is present in a list or not.

l = ["Aryan", "Larry", "Rohan", "Shubham", "Divya"]
name = input("Enter your name : ")

if(name in l):
    print("Your name is present in the given list")

else:
    print("Your name is not present in the given list")
