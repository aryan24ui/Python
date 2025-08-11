'''Write a program to find whether a given username contains less than 10
characters or not.'''

username = input("Enter your user name : ")

if(len(username)<10):
    print("User name contain less than 10 characters")

else:
    print("User name does not contain less than 10 characters")