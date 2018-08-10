class classmeth:
    a=10 #Static variable
    def __init__(self): #constructor
        self.b=20
        classmeth.c=30
    def m2(self): #instance method
        self.f=60    
    @classmethod #class method
    def meth(cls): #here we can give any name to class meth or "cls" to represent a class meth
        cls.d=40
        classmeth.e=50
    @staticmethod
    def m3(): #static method
        classmeth.g=70
#we can call 
        
t=classmeth()
classmeth.a=30
t.m2()
classmeth.meth()
t.m3()
print(classmeth.a+t.b+classmeth.c+classmeth.d+classmeth.e+t.f+classmeth.g)
print(t.a+t.b+t.c+t.d+t.e+t.f+t.g)
print(classmeth.__dict__) #Dictionary for class
print(t.__dict__) #Dictionary for Method - mute


        
        
