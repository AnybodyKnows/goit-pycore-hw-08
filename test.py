class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Define a __str__ method to customize the string representation
    def __str__(self):
        return f"MyClass object with attributes: attribute1={self.attribute1}, attribute2={self.attribute2}"

# Create an instance of MyClass
my_object = MyClass("value1", "value2")

# Using the print function
print(my_object)

# Or you can directly call str() on the object
print((my_object))