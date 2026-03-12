class Foo:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def printFoo(self):
        print("Foo name is " + self.name + " foo color is " + self.color)

obj = Foo("Philip", "Blue")
obj.printFoo()
