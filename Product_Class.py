class Product:
      def __init__(self, name, price, quantity):
         self.name = name
         self.price = price
         self.quantity = quantity
   
      def calculate_total_value(self):
           return self.price * self.quantity
      
#Create an instance of the Product class for new items
laptop = Product("Apple MacBook Pro", 33000.00, 5)

print("--- Product Information ---")
print(f"Product name: {laptop.name}")
print(f"Price per unit: R{laptop.price:,.2f}")
print(f"Quantity in stock: {laptop.quantity}")

# Calculate and display the total value of the stock
total_value = laptop.calculate_total_value()
print(f"Total value of stock: R{total_value:,.2f}")
print("---------------------------")