#Write a program to accept marks of 6 students and display them in a sorted manner.
Student = []

s1 = int(input("Enter Marks: "))
Student.append(s1) 
s2 = int(input("Enter Marks: "))
Student.append(s2) 
s3 = int(input("Enter Marks: "))
Student.append(s3) 
s4 = int(input("Enter Marks: "))
Student.append(s4) 
s5 = int(input("Enter Marks: "))
Student.append(s5) 
s6 = int(input("Enter Marks: "))
Student.append(s6) 

Student.sort()
print(Student)
