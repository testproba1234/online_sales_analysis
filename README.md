# Online Sales Analysis

## Description
This project is an analysis tool for managing products and sales in an online store. It allows users to manage products, calculate inventory values, add items to a shopping cart, and calculate the total value of the cart.

## Classes

### Product
- `name`: The name of the product.
- `price`: The price of the product.
- `quantity`: The quantity of the product in stock.
- `display_info()`: Method to display product details.
- `update_quantity()`: Method to update the product's quantity.

### ProductManager
- `products`: A list of all available products.
- `add_product()`: Method to add a product.
- `display_all_products()`: Method to display all products.
- `get_inventory_value()`: Method to calculate the total value of all products in the inventory.
- `remove_product()`: Method to remove a product by name (added in a separate branch).

### Cart
- `cart_items`: A list of products in the cart.
- `add_to_cart()`: Method to add a product to the cart.
- `calculate_cart_value()`: Method to calculate the total value of the items in the cart.
- `display_cart()`: Method to display the cart's contents.

## Usage
1. Create a `ProductManager` instance.
2. Add products to the inventory.
3. Use the `Cart` class to add products to the cart and calculate the total.

## Installation
Clone the repository to your local machine and use Python 3 to run the project.
