z=10
class Parent:
    print("In Parent Class")
    value1=int(input("value1="))
    value2=int(input("value2="))
    print(value1)
    print(value2)

parent_=Parent()

class Child (Parent):
    print("In child class")
    value3=int(input("value3="))
    sum1=parent_.value1+parent_.value2+value3

child_=Child()

class Child2 (Child):
    def addMore(self):
        self.value4=int(input("value4="))#instance variable
        self.result=child_.sum1+self.value4
        print("Total sum=",self.result)
    
child2_=Child2()
child2_.addMore()

class Static (Child2):
    value5=10 #static variable
    def __init__(self):
        self.value6=10
        self.sum2=self.value6+Static.value5+child2_.result+z
        
static_=Static()
print("value5=",Static.value5,"value6=",static_.value6,"z:",z)
print("sum2=",static_.sum2)
print(Static.__dict__)












