#List, Tuple, Set:
l=list(range(100,200,10))
t=tuple(range(100,200,10))
s=set(range(100,200,10))

print('l:',l)
print('t:',t)
print('s:',s)

#len()
print('l:',len(l))
print('t:',len(t))
print('s:',len(s))

#count()
print('l:',l.count(10))
print('t:',t.count(10))
#print('s:',s.count(s))  --> Not avaiable

#reverse()
l.reverse()
print(l)
#t.reverse()--> Not avaiable
print(t)

#sort()
l.sort()
print(l)
l.sort(reverse=True)
print('reverse of l:',l)
x=tuple(sorted(t))
print(x)
x=tuple(sorted(t,reverse=True))
print(x)

#Remove()
l.remove(190)
print(l)
#t.remove(190) --> Not avaiable
#print(t)

#Index()
print(l.index(100))
print(t.index(100))

#Append list --> To add elements into list
l.append(500)
l.append(600)
l.append(400)
print(l)

#To add numbers which are divisible by 3 in a given range:
for x in range(1,101):
    if x%3==0:
        l.append(x)
print(l)

#extend()
l2=[1000,2000,3000]
l.extend(l2)
print(l)

#insert()
l.insert(10,5000) #--> This will allow us to insert at required indexes
print(l)

#List comprehension:
y=[x for x in range(1,100) if x%3==0]
print(y)

#To print im Matrix form:

l4=[[10,20,30],[40,50,60,70],[70,80,90]]
    
for i in range(len(l4)):
    for j in range(len(l4[i])):
        print(l4[i][j],end=' ')
    print()













