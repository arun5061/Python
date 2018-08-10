class Parent:
    x=10
    y=20
    z=x+y
parent_=Parent()

class Child1:
    a=10
    b=20
    c=parent_.z+a+b
    print(c)

child1_=Child1()

class Child2:
    def __init__(self):
        self.g=10
        print("hi")
    def sum(self):
        self.d=10
        e=child1_.c+self.d+Child2.f+self.g
        print(self.g)
        print(e)

    
child2_=Child2()
Child2.f=10
child2_.g=100
child2_.sum()

