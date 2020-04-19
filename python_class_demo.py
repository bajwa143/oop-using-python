# name rules for class are same as for variables in python
# use of capital letter for class is convention

# Docstrings are enclosed in triple quotes, which Python
# looks for when it generates documentation for the functions in your programs
# it is like java docs but write within function defination


class Person:
    """ Person class to model any person """

    def __init__(self, name, age=1):    # default value for age
        """ initialize Person """
        # self must be first parameter, it give access to member variable and methods of class
        self.name = name
        self.age = age

    def print_detail(self):
        print(f"I am {self.name}, {self.age} years old")
