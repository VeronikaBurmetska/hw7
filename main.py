class Parent:
    def parent(self):
        print("Cities:")

class Child:
    def child(self):
        print("Kyiv, London, Paris, Rome…")

class Cities(Child, Parent):
    pass

fruits = Cities()
fruits.parent()
fruits.child()