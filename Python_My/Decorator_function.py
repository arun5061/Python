def decor(div):
    print('hi1')
    def inner(a,b):
        print('h2')
        if b==0:
            return("can't div by zero")
        else:
            return div(a,b)
    print('hi')
    return inner
#@decor
def div(a,b):
    return a/b
divfun=decor(div)
print(divfun(10,2))
print(div(15,5))
#y=divfun(10,2)
#print(y)
#print(div(10,20))
#print(divfun(10,0))
