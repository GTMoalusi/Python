class Student:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def display_info(self):
      print("--- Student Information ---")
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")
      print("---------------------------")

student_1 = Student("Lefa", 18)

student_1.display_info()

print(f"Student's Name: {student_1.name}, Age: {student_1.age}")