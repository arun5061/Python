import pickle,Emp
e=Emp.emp(11,'arun','ori')
e1=Emp.emp(11,'kumar','hyd')
e.display()
e1.display()
f=open('emp.txt','rb')
print('Emp details')
while True:
	try:
		obj=pickle.load(f)
		obj.display()
	except EOFError:
		print('Done with all objects...')
		break
f.close()
