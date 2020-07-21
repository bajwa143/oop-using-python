# A mix-in is a class that defines only a small set of additional methods for its child classes
# Mix-in classes don’t define their own instance attributes nor require their __init__ constructor to be called
# Mix-ins can be composed and layered to minimize repetitive code and maximize reuse

# A mixin is a class that inherits from two or more other classes, combining their feature
# A Mixin is a set of properties and methods that can be used in different classes which don't come from a base class.

# Mix-ins does not exist in multiple inheritance languages. So it is not C# and Java

class SalaryMixin:
	def draw_salary(self, amount):
		if amount > 0 and amount <= self.salary:
			self.salary = self.salary - amount
			print("Salary Drawn Successfully")
			# using interpolated format strings or f-strings in short
			print(f"New Salary after withdrawl {self.salary}")
		else:
			print("Incorrect salary amount to draw")