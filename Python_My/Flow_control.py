#Flow control

n=10

if n>=1 and n<=100:
    print(' %i In between' %n)
else:
    print("not present")
#For each element in the sequence do some action
x="hello world"
count=0
for s in x:
    count+=1
    print(s)
print("Number of characters:",count)

v="how are you"
i=0
for b in v:
    if 2<=i<=4:
        print(b)
    i+=1  
print()

for y in range(5,10):
    print(y)

for z in range(25):
    if z%2==0:
        print(z)
print()
for s in range(20,0,-1):
    print(s)

#list=eval(input("enter list:"))
list=[1,2,3]
sum=0
for u in list:
    sum+=u
print(type(list))
print("sum is:",sum)

#While loop
n=eval(input("Enter n Value:"))
i=0
sum=0
while i<=n:  #Loop will continue untill condition is True
    sum+=i
    i+=1
print("sum of n values:",sum)


name=''
while name!='Arun':
    name=input("Enter name:")
print("Thanks for confrm")

name=''
pwd=''
while (name!='vishnu') or (pwd!='python'):
    name=input("Enter name=")
    pwd=input("Enter pwd=")
print('Thanks for confirm')


        









    
