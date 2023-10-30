class ProductItem:
    def __init__(self, id, name, category_id, price):
        self.id = id  # unique identifier for a product
        self.name = name  # name of the product
        self.category_id = category_id  # category identifier (like Footwear, Apparel, etc.)
        self.price = price  # price of the product

class Cart:
    def __init__(self):
        self.cart_items = []  # initialize an empty cart

    def add_product(self, product, quantity):
        """Add a product and its quantity to the cart."""
        self.cart_items.append((product, quantity))  # each item is a tuple of (product, quantity)

    def remove_product(self, product):
        """Remove all quantities of a product from the cart."""
        # Using list comprehension to filter out the specified product
        self.cart_items = [item for item in self.cart_items if item[0] != product]

    def view_products(self):
        """Return a list of products in the cart."""
        return self.cart_items

class OnlineShop:
    def __init__(self):
        self.available_products = []  # list of products available in the shop
        self.product_categories = ['Footwear', 'Apparel', 'Electronics', 'Accessories']
        self.admin_password = "secureAdminPass"
        self.registered_users = [Shopper("Alice_Shopper", "secureShopperPass")]
        self.current_shopper = None  # currently logged in shopper
        self.admin_session_active = False  # flag to check if admin is logged in

    def view_catalog(self):
        """Return a list of products available in the shop."""
        if not self.available_products:
            return "No products in the catalog currently."
        return [(product.name, product.price) for product in self.available_products]

    def shopper_login(self, username, password):
        """Allow a shopper to log in if credentials match."""
        user = next((u for u in self.registered_users if u.username == username and u.password == password), None)
        if user:
            self.current_shopper = user
            self.admin_session_active = False
            return f"Welcome to the OnlineShop, {username}."
        else:
            return "Login failed: Invalid credentials."

    def admin_login(self, password):
        """Allow admin access if the password matches."""
        if password == self.admin_password:
            self.admin_session_active = True
            self.current_shopper = None
            return "Admin access granted."
        else:
            return "Admin login failed: Incorrect password."

    def add_product(self, product):
        """Allow admin to add a product to the catalog."""
        if self.admin_session_active:
            self.available_products.append(product)
            return f"Product {product.name} added to the catalog."
        else:
            return "Error: Admin access required."

    def add_product_to_cart(self, product_name, quantity):
        """Allow a logged-in shopper to add a product to their cart."""
        if self.current_shopper:
            product = next((p for p in self.available_products if p.name == product_name), None)
            if product:
                self.current_shopper.personal_cart.add_product(product, quantity)
                return f"Added {product_name} to the shopping cart."
            else:
                return "Error: Product not found in the catalog."
        else:
            return "Please log in to add items to the cart."

    def view_shopper_cart(self):
        """Allow a logged-in shopper to view their cart."""
        if self.current_shopper:
            items = self.current_shopper.personal_cart.view_products()
            return [(item[0].name, item[1]) for item in items]
        else:
            return "Please log in to view your cart."

    def shopper_checkout(self, payment_method):
        """Allow a logged-in shopper to proceed to checkout."""
        if self.current_shopper:
            total_price = sum(item[0].price * item[1] for item in self.current_shopper.personal_cart.view_products())
            return f"Checkout successful via {payment_method}. Total payable: {total_price}."
        else:
            return "Please log in to proceed to checkout."

    def add_category(self, category):
        """Allow admin to add a new product category."""
        if self.admin_session_active:
            self.product_categories.append(category)d
            return f"Product category '{category}' added successfully."
        else:
            return "Error: Admin access required."

class Shopper:
    def __init__(self, username, password):
        self.username = username  # shopper's username
        self.password = password  # shopper's password
        self.personal_cart = Cart()  # every shopper has a personal cart

# Usage demonstration:
store = OnlineShop()

# Admin logs in to add products
print(store.admin_login("secureAdminPass"))

# Adding products to Footwear category
print(store.add_product(ProductItem(1, "Trendy Boots", 1, 1200)))
print(store.add_product(ProductItem(2, "Sports Shoes", 1, 1500)))

# Adding products to Apparel category
print(store.add_product(ProductItem(3, "Summer T-shirt", 2, 500)))
print(store.add_product(ProductItem(4, "Winter Jacket", 2, 2500)))

# Adding products to Electronics category
print(store.add_product(ProductItem(5, "Bluetooth Headphones", 3, 1800)))
print(store.add_product(ProductItem(6, "Smart Watch", 3, 3000)))

# Adding products to Accessories category
print(store.add_product(ProductItem(7, "Leather Wallet", 4, 700)))
print(store.add_product(ProductItem(8, "Sunglasses", 4, 1000)))

# Admin viewing catalog
print(store.view_catalog())

# Shopper logs in, views the catalog, adds products to cart, and checks out
print(store.shopper_login("Alice_Shopper", "secureShopperPass"))
print(store.view_catalog())  # Shopper viewing catalog
print(store.add_product_to_cart("Trendy Boots", 1))
print(store.add_product_to_cart("Smart Watch", 1))
print(store.view_shopper_cart())
print(store.shopper_checkout("Credit Card"))
