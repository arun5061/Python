#Tuple
t=(20,40,10,41,100,20)
l=sorted(t)
print(tuple(l))

r=eval(input('Entre numbers to find sum and avg:'))
sum=0
l=len(r)
for x in r:
    sum=sum+x
print('sum:',sum)
print('Avg:',sum/l)

#To sort in reverse order i.e decending order
x=(10,40,60,20)
print(x)
x2=tuple(sorted(x,reverse=True))
print(x2)





