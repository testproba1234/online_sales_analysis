class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Prikazuje informacije o proizvodu."""
        return f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity):
        """Ažurira količinu proizvoda."""
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

# Testiranje klase (opciono, možeš dodati ovo privremeno)
if __name__ == "__main__":
    product1 = Product("Laptop", 999.99, 10)
    print(product1.display_info())
    product1.update_quantity(8)
    print(product1.display_info())
