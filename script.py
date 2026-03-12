class Foo:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    
    def printFoo(self):
        print("Foo name is " + self.name + " foo color is " + self.color + " foo size is " + self.size)

obj = Foo("Philip", "Blue", "large")
obj.printFoo()

print("Hello World")