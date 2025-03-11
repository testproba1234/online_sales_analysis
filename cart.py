class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product):
        self.cart_items.append(product)
        print(f"Product {product.name} added to the cart.")

    def total_value(self):
        total = sum([item.price * item.quantity for item in self.cart_items])
        return total

    def display_cart(self):
        for item in self.cart_items:
            print(f"Product: {item.name}, Price: {item.price}, Quantity: {item.quantity}")
        print(f"Total value: {self.total_value()}")
