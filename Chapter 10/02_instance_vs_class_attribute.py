class Employee:
    language = "Python" # language and salary are class attribute as the directly belong to class
    salary = 1200000

aryan = Employee()
aryan.language = "JavaScript"
print(aryan.language, aryan.salary)

#Note: Instance attributes, take preference over class attributes during assignment 
# & retrieval.
