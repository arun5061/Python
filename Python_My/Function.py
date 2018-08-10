#Function:
def hi():
    print ('Hello')
hi()

def fun():
    print ('Hello world')
for i in range(4):
    fun()

def wish(name):
    print('Hello',name,'Gud mrng!')
for i in range(3):
    y=wish(input('Enter name:'))
print("Thanks for using my app")

def sum(x,y):
    s=x+y
    return s,x,y
print(sum(100,600))
s,x,y=sum(800,700)
print('s:',s,'x:',x,'y:',y)
y=sum(10,20)
print(y)
for i in y:
    print(i)
#print('sum:',s,'x:',x,'y:',y)
z=sum(30,20)
print(z)

#Resursive Function:
#Factorial example
#Anonymous function -----> lambda
#Filter,Map,Reduce

#Filter()  ----> Based on return condtion, if cond. is true then only that value will be
#considered

def fill(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,200,500,600,20,57,89,13]
print(l)
t=tuple(filter(fill,l))
print(t)

#Same above function using lambda()

t1=tuple(filter(lambda x:x%2==0,l))
print(t1)

#Map() -----> It will mve values based on expression

t3=tuple(map(lambda x:x*x,l))
print(t3)

def mul(a,b):
    result=a*b
    return result

t4=(1,2,3,5,6)
t5=(7,8,9,1,11)
t7=tuple(map(mul,t4,t5))
print(t7)
t6=tuple(map(lambda x,y:x*y,t4,t5))
print(t6)




    
    
