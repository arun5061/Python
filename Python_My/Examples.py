s=set() #Example for set
for i in range(5):
    s.add(i) #set has no order for insertion so we go for add
    s.add(16)
    print (s)

#Frozen - Group of unique values no one is allowed to make changes
r={1,2,3} #EX for frozen set
r=frozenset(r)
print(r)

#x=[0,1,2] #Bytes
b=bytes([0,1,2])
print(type(b))
print(b)
for i in b: print(i,end= ' ')
print()
a=[1,2,3,15,'arun','mohan'] #list
print(type(a))
a[1]=5
print(a)
b=(1,2,3,15,'arun','mohan') #tuple
print(type(b))
#b[1]=5 - does not support
print(b)
c={'Id':5061,'Name':'Arun', 'Company':'TCS'}
print(type(c))
class a: #Ex for return
    def add(self):
        self.x=100
        self.y=200
        return(self.x+self.y)
a1=a()
a1.add()
sum1=a1.add()
print("sum1",sum1)

def add(x,y):
    return(x+y)
sum2=add(10,20)
print(sum2)

def f():
    a=10
print(f())

def f2(): print("hello")
f2()

#Dictionary dict{}
d={'Id':5061,'Name:':'Arun'}
d[5091]='Vishnu'
print(d)

c=20//10
print(c)

e=2.2**3.2
print(e)

a=int(input("value10="))
b=int(input("value20="))
c=int(input("value30="))

if a<b<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)

# Same above logic
#Trernary operator

x=a if a<b<c else b if b<c else c
print('x:',x)

#Evaluale

sum1=eval("a+b+c")
print(sum1)

ex=input("enter expression:")
result=eval(ex)
print(result)

x=eval(input('enter:'))
print(type(x))
for b in x:
    print(b)

x,y,z=[eval(e) for e in input("enter").split(',')]
print(x,y,z)

for n in range(2):
    print(n)
