# --- Basic Calculator & Unit Convertor ---

def calculator ():
   while True:
      print("Choose your selection from below options:")
      print("1. Arithmetic.")
      print("2. Conversion.")
      print("3. Exit.")

      choice = input("Enter 1, 2, or 3:")

      if choice == "1":
         arithmetic()
      elif choice == "2":
         conversion()
      elif choice == "3":
         print("Good bye")
         break
      else:
         print("Invalid choice.")

def arithmetic():
   num_1 = float(input("Enter your first number: "))
   num_2 = float(input("Enter your second number: "))
   operations = input("Enter your operation (+, -, /, *, %): ")

   if operations == "+":
      results = num_1 + num_2 
   elif operations == "-":
      results = num_1 - num_2
   elif operations == "/":
      if num_2 == 0 or num_1 == 0:
         print("You cannot divide by zero!")
         return
      else:
         results = num_1 / num_2
   elif operations == "*":
      results = num_1 * num_2
   elif operations == "%":
      results = num_1 % num_2
   else:
      print("Choose an operation from the given list!")
   
   print(f"Results: {results}")
   
def conversion():
   print("Available conversions:")
   print("1. Kilometers to Miles")
   print("2. Miles to Kilometers")
   print("3. Celsius to Fahrenheit")
   print("4. Fahrenheit to Celsius")

   conversion_choice = input("Enter your conversion choice (1, 2, 3, or 4): ")

   if conversion_choice == '1':
      kilometers = float(input("Enter kilometers: "))
      miles = kilometers * 0.621371
      print(f"{kilometers} km is equal to {miles:.2f} miles")
   elif conversion_choice == '2':
      miles = float(input("Enter miles: "))
      kilometers = miles / 0.621371
      print(f"{miles} miles is equal to {kilometers:.2f} km")
   elif conversion_choice == '3':
      celsius = float(input("Enter Celsius temperature: "))
      fahrenheit = (celsius * 9/5) + 32
      print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
   elif conversion_choice == '4':
      fahrenheit = float(input("Enter Fahrenheit temperature: "))
      celsius = (fahrenheit - 32) * 5/9
      print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
   else:
      print("Invalid conversion choice.")
   
# Run the calculator program
calculator()