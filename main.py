from product import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
manager.add_product(Product("Laptop", 1200.00, 5))
manager.add_product(Product("Mouse", 25.99, 15))
manager.add_product(Product("Keyboard", 45.50, 10))

# Prikaz svih proizvoda
print("Available Products:")
manager.display_products()

# Prikaz ukupne vrednosti inventara
print(f"\nTotal Inventory Value: ${manager.total_inventory_value():.2f}")

from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje instance ProductManager
product_manager = ProductManager()

# Dodavanje proizvoda
product_manager.add_product(Product("Laptop", 1000, 5))
product_manager.add_product(Product("Phone", 500, 10))
product_manager.add_product(Product("Headphones", 100, 3))

# Kreiranje instance Cart
cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_item(product_manager.products[0])  # Laptop
cart.add_item(product_manager.products[1])  # Phone
cart.add_item(product_manager.products[2])  # Headphones

# Prikazivanje sadržaja korpe
cart.display_cart()
