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
