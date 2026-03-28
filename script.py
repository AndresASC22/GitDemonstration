class Foo:
    def __init__(self, name, color, size, age):
        self.name = name
        self.color = color
        self.size = size
        self.age = age
    
    def printFoo(self):
        print("Foo name is " + self.name + " foo color is " + self.color + " foo size is " + self.size +
                " and age is " + str(self.age))

obj = Foo("Philip", "Blue", "large", 20)
obj.printFoo()

print("Hello World")