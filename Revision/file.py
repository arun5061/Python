with open('insert.txt','w') as f:
	for i in range(3): 
		f.write(input('Enter data:'))
		f.write('\n')
l=[]
with open('insert.txt','r') as rf:
	for line in rf:
		l.append(line)
print(l)

l.insert(0,'This is 0 line..:)''\n')
print(l)

with open('insert1.txt','w') as wf:
	wf.writelines(l)

with open('insert.txt','r') as rf:
	l2=rf.readlines()
print('l2:',l2)
l2.insert(0,'Super bains living on earth:''\n')

with open('insert2.txt','w') as wf:
	wf.writelines(l2)

f=open('insert2.txt','r')
f_cont=f.read(10)
while len(f_cont)>0:
	print(f_cont,end='*')
	f_cont=f.read(10)
f.close()

