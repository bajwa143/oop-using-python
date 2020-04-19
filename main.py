from python_class_demo import Person

# create instance of class
a_person = Person("Ibraham", 43)
a_person.print_detail()

# crate a person without suppling age, default value will be used for age
b_person = Person("Marco")
b_person.print_detail()