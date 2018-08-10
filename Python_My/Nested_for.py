#Nested for loop:
for i in range(5):
    for j in range(5):
        #print("Value of i=%i, j=%i" %(i,j))
        print("i={},j={}".format(i,j), end='\n')

print("Hello", end='....') #Usage of end statement
print("GM")

#To print n stars:
#*
#**
#***
b=n=eval(input("Enter n value:"))

for i in range(1,n+1):
    for j in range(i):
        print("*", end=' ')
    print()

for i in range(1,n+1):
    print("*"*i)
    print()

for i in range(n):
    print("*"*n)

for i in range(n):
    for j in range(n):
        print("* ", end=' ')
    print()
    
for i in range (n):
    t=n
    s=n
    s-=i
    for j in range(s):
        print(t,end=' ')
        t-=1
    print()  
    
print()
n=eval(input("Enter n value:"))

for i in range(50,4,-5):print(i) 

for i in range(n):
    print("* "*n,end='\n')
    print()
    n-=1
list=[1,2,3]

for i in list:
    if i==1:
        print(i)
    elif i==2:
        print(i)
    elif i==3:
        print(i)

        
    
        
        
    







