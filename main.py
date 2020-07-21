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

from python_class_demo import Person, Student, Teacher, Manager
# we can also use '*' to import all classes from a module
#from python_class_demo import *
# but it is not recommend, because it is not clear which classes we are importing and using

# create instance of class
a_person = Person("Ibraham", 43)
a_person.print_detail()

# crate a person without suppling age, default value will be used for age
b_person = Person("Marco")
b_person.print_detail()

# we can directly access value of class attribute
a_person.name = "New Ibraham"
a_person.age = 44
print("Values after directly updating")
a_person.print_detail()


# we can also use class methods to change values
b_person.set_name("New Marco")
b_person.set_age(2)
print("Values after updating via methods")
print("New Name: "+b_person.get_name())
print(f"New Age: {b_person.get_age()}")


# demo Student class
std = Student("Rafeel",21,"s-343")
std.print_detail()
print(std)

# print total count
print("Total instance created are {}".format(Person.total_count))

# create teacher class to demo mixin
tch = Teacher("Saad",34,23000)
tch.print_detail()
tch.draw_salary(18000)

# Manager class
mgr = Manager("Raza",40,20000)
mgr.print_detail()
mgr.draw_salary(18000)