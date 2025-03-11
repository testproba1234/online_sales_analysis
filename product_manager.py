from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Dodaje novi proizvod u listu proizvoda."""
        self.products.append(product)

    def display_products(self):
        """Prikazuje sve proizvode u inventaru."""
        if not self.products:
            print("No products available.")
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        """Izračunava ukupnu vrednost svih proizvoda u inventaru."""
        return sum(product.price * product.quantity for product in self.products)

# Testiranje klase (opciono)
if __name__ == "__main__":
    manager = ProductManager()
    manager.add_product(Product("Phone", 699.99, 5))
    manager.add_product(Product("Tablet", 399.99, 3))
    manager.display_products()
    print(f"Total Inventory Value: ${manager.total_inventory_value():.2f}")

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product {name} removed.")
                return
        print(f"Product {name} not found.")
