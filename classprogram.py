x = 1000  # Bydefault, variable outside the class is a global variable

# Creating Class
class FirstClass:
    b = 30  # Class Variable

    def assign(self):  # By default, all are Instance Method
        global a  # Global Variable
        a = 10
        self.b = 40

    @staticmethod
    def display():  # Static method used with @staticmethod keyword
        localvar = 100  # Local Variable
        print(a, localvar)

    @staticmethod
    def static_self(self):
        print("self", self)

    def instance_method(self):
        print(self.b)

    def global_local_var(self, x):
        print("Local Variable", x)
        print("Global Variable",
              globals()['x'])  # Use globals()[''] when both local & global variable has the same name


Obj = FirstClass()  # Creating Named Object

Obj.assign()
FirstClass.display()  # static method is called using ClassName
FirstClass.static_self(100)
Obj.instance_method()
print("Printing Class Variable Outside Class", Obj.b)
Obj.global_local_var(-9)

FirstClass().display()  # Nameless Object can be used with ClassName()

# comparing objects of the same class
obj1 = FirstClass()
obj2 = FirstClass()
obj3 = FirstClass()
obj4 = obj3

print(obj4 is obj3)  #True
print(obj3 is obj1)  #False
print(obj2 is not obj1)  #True


print(id(obj1))
print(id(obj2))
print(id(obj3))
print(id(obj4))

