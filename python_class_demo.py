"""
Copyright (c) 2020 Muhammad Saqib Bajwa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# name rules for class are same as for variables in python
# use of capital letter for class is convention

# Docstrings are enclosed in triple quotes, which Python
# looks for when it generates documentation for the functions in your programs
# it is like java docs but write within function defination

"""Person class to represent a person - a module-level docstring"""
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

    # change string representation of this class instance
    # this representation is used by str() and print() function
    def __str__(self):
        return (f'{self.name},{self.age}')

    # __repr__ method returns the code representation of an instance, 
    # usually the text used to re-create the instance of class
    def __repr__(self):
        # return (f'Student{self.name,self.age}')
        return 'Student(%r,%r)' % (self.name, self.age)

# INHERITANCE
# for inheritance parent class must part of current file and appear before child class

class Student(Person):      # parent class name should be given in parameter
    def __init__(self, name, age, roll_no):
        # initialize variables in parent class
        super().__init__(name, age) # super() is used to make connection/call to parent class
                                    # something like super in Java and base in C#
        self.roll_no = roll_no

    # we can override parent class method
    def print_detail(self):
        # we can write all detail here or can also call parent method too
        super().print_detail()
        print("My roll is "+str(self.roll_no))
