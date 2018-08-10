#Lambda - For lamda we need to give more then one argument and a,b should be same length
a=[10,2]
b=[5,2]
y=list(map(lambda a,b:(a**2+b**2+2*a*b),a,b))
print(y)
l=list(range(50))
z=list(filter(lambda x: x%2==0,l))
print(z)