# class Person:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       print(f"Hello! {self.name}, aged {self.age}, has been created.")


#    def __del__(self):
#       print(f"Goodbye! {self.name} is being deleted from memory.")

# # --- Example Usage ---

# # Create a new Person object.
# # This will call the __init__ constructor.
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# # The objects still exist here. Nothing will be printed.
# print("\nObjects are currently in use...")

# # We can manually delete an object to force the __del__ method to be called.
# # This is not common practice, as Python's garbage collector handles this.
# print("\nManually deleting person1...")
# del person1

# # The program is about to end. The remaining object (person2) will
# # be garbage collected, and its destructor will be called automatically.
# print("\nProgram is ending. The last object will be deleted automatically.")

# class Animal:
#    def __init__(self, name):
#       self.name = name

#    def make_sound(self):
#       print("Generic animal sound")

# class Dog(Animal):
#    def make_sound(self):
#       print("Woof woof")

# lassie = Dog("Lassie")
# lassie.make_sound()

# class Flyer:
#    def fly(self):
#       print("Flying...")

# class Swimmer:
#    def swim(self):
#       print("Swimming...")

# class Duck(Flyer, Swimmer):
#    pass

# duck = Duck()
# duck.fly()
# duck.swim()

