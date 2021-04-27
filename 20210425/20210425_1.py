#overriding

class Parent:
    def show(self):
        print("Hello Parent")

class Child1:
    def show(self):
        print("Hello child1")

class Child2:
    def show(self):
        print("Hello child2")


obj=Parent()
obj1=Child1()
obj2=Child2()

obj.show()
obj1.show()
obj2.show()
