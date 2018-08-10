#import sys
#sys.setrecursionlimit(1500)
def factorial(x):
    if x == 0:
        result=1
    else:
        result=x*factorial(x-1)
    return result
print(factorial(5))
