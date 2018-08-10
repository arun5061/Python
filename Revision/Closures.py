'''Closures has inner functions where it holds 
values of outer function in Memory'''
def outer_func(func1,func2):
    print(func1.__name__)
    print(func2.__name__)
    def inner_func(*args):
        print(*args)
        print(func1(*args))
        print(func2(*args))
    return inner_funcs

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

add_out = outer_func(add,sub)  
add_out(1,5)
