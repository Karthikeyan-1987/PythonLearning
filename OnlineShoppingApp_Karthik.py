class ProductItem:
    def __init__(self, product_id, product_name, category, price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = category
        self.product_price = price

    def __repr__(self):
        return f"ProductItem(id={self.product_id}, name={self.product_name}, category={self.product_category}, price={self.product_price})"


class Admin:
    AllAdmin_passwords = ["AdminPass", "ADPass", "ExecutivePass"]
    global admin_active
    Available_Products = []

    def __init__(self, password=None):
        if password is None:
            self.RegisteredUsers = [User("Karthi", "psw"), User("Ilakkiya", "loginpsw")]
        else:
            self.admin_active = True
            self.Admin_Pass = next((x for x in self.AllAdmin_passwords if x == password), None)
            if self.Admin_Pass:
                print("Admin has logged into the system now")

    def Admin_Add_product(self, product):
        self.Available_Products.append(product)
        return f"Product {product.product_name} Added to the Online Store"

    def View_Products(self):
        return [(product.product_name, product.product_price) for product in self.Available_Products]

    def User_Login(self, username, pass_word):
        return (next((user for user in self.RegisteredUsers if user.UserName == username and user.UserPsw == pass_word),
                     None))


class UserCart:
    def __init__(self, user):
        self.User_Cart = []
        self.user = user

    def add_to_cart(self, product_name, quantity, price):  # working on this
        product = next((p for p in Admin.Available_Products if product_name == p.product_name), None)
        print("p.product_name", product.product_name)
        self.User_Cart.append(
            (product.product_id, product.product_name, product.product_category, product.product_price, quantity))
        print("add_to_cart", self.User_Cart)
        return f"{product_name} - {quantity} has been added to the cart."

    def view_cart(self):
        return self.User_Cart

    def checkout(self, payment):
        # print(item[3] * item[4] for item in self.view_cart())
        total_price = sum((item[3] * item[4]) for item in self.view_cart())
        return f"Order has been placed successfully and Payment of ${total_price} made through {payment} for the user {self.user.UserName}"


class User:
    def __init__(self, UserName, Password):
        self.UserName = UserName
        self.UserPsw = Password
        self.PersonalCart = UserCart(self)


Obj_Admin = Admin("AdminPass")
print(Obj_Admin.Admin_Add_product(ProductItem(1, "Ipod", 1, 4000)))
print(Obj_Admin.Admin_Add_product(ProductItem(11, "Ladies Shoe", 2, 40)))
print(Obj_Admin.Admin_Add_product(ProductItem(12, "Apple", 3, 4)))
print(Obj_Admin.Admin_Add_product(ProductItem(14, "Onion", 4, 6)))
print(Obj_Admin.Admin_Add_product(ProductItem(17, "Laptop", 1, 8000)))

print("Total Available Products in the Shop\n", Obj_Admin.View_Products())

User_Ilakkiya = Admin().User_Login("Ilakkiya", "loginpsw")

if User_Ilakkiya:
    print("User Authenticated, Login Successful")

print(User_Ilakkiya.PersonalCart.add_to_cart("Ipod", 2, 4000))
print(User_Ilakkiya.PersonalCart.add_to_cart("Apple", 20, 4))
print(User_Ilakkiya.PersonalCart.add_to_cart("Laptop", 8, 8000))
print(User_Ilakkiya.PersonalCart.add_to_cart("Onion", 12, 6))
print(User_Ilakkiya.PersonalCart.view_cart())

User_Karthik = Admin().User_Login("Karthi", "psw")

if User_Karthik:
    print("User Authenticated, Login Successful")

print(User_Karthik.PersonalCart.add_to_cart("Ipod", 21, 4000))
print(User_Karthik.PersonalCart.add_to_cart("Apple", 202, 4))
print(User_Karthik.PersonalCart.add_to_cart("Laptop", 2, 8000))
print(User_Karthik.PersonalCart.add_to_cart("Onion", 82, 6))
print(User_Karthik.PersonalCart.view_cart())

print(User_Ilakkiya.PersonalCart.checkout('NetBanking'))
print(User_Karthik.PersonalCart.checkout('CreditCard'))

