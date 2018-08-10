list=[]
x=int(input('Enter no of students:'))
for i in range(x):
	list.append(input('Enter student name{}:'.format(i)))
print(list)
d=dict()
s=0
for j in list:
	val=input('Enter value{}:'.format(s))
	s+=1
	d[j]=val
print('d:',d)
for k,v in d.items():
	print('Key:',k,'\t','value:',v)                         


