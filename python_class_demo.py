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

    # we can define method to set and get values like setter and getter in other languages
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# INHERITANCE
# for inheritance parent class must part of current file and appear before child class

class Student(Person):      # parent class name should be given in para
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no = roll_no

    # we can override parent class method
    def print_detail(self):
        # we can write all detail here or can also call parent method too
        super().print_detail()
        print("My roll is "+str(self.roll_no))

