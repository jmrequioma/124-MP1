class Student:
	def __init__(self, name, age, gpa, grade_level):
		self.name = name
		self.age = age
		self.gpa = gpa
		self.grade_level = grade_level

	def display(self):
		print(self.name)
		print(self.age)
		print(self.gpa)
		print(sefl.grade_level)

p1 = Student("John", 15, 1.50, "Senior")
p1.display()