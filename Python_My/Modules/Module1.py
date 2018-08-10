#Module--> group of functions Module 1 if __name__=__main__ loaded
#dirctly if not loaded indirectly and __name__ will have module name
#Examples of importing modules import module1,modue2,... import module1
#as mod1 from module1 import f1() from module1 import f1() as f

def f1():
    if __name__=='__main__':
        print("This module is loaded directly")
        print('value of __name__:',__name__)
    else:
        print("This module is loaded indirectly")
        print('value of __name__:',__name__)
f1()

def f2():
    print("Initial version-10")
f2()

class InsufficientFunds(Exception):
    def __init__(self,arg):
        self.msg=arg

class YouCantDivbyZero(Exception):
    def __init__(self,arg):
        self.msg=arg

'''
This is Main module importing Module1
This module is loaded indirectly
value of __name__: Module1
Initial version-2
Explictly calling function in Module1
This module is loaded indirectly
value of __name__: Module1
Entering into sleep first time
This module is loaded indirectly
value of __name__: Module1
Initial version-3
Entering into sleep second time
This module is loaded indirectly
value of __name__: Module1
Initial version-4
'''
