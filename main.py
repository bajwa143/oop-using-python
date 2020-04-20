from python_class_demo import Person, Student

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