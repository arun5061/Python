def arg():
	print('hi')
arg()

#Positional argu:
def f1(a,b):
	return a+b,a,b #It returns multiple values as tuple output
y=f1(10,5)
for i in y:
	print(i)

#Keyword argu:
def f2(x,y):
	z=x+y
	return z
print(f2(y=10,x=5))

#Default argu: -> It will take argu which we pass
def f3(i,j=10):
	k=i+j
	return k
print(f3(5,20))

#Variable length argu:
def f4(*n):
	s=0
	for i in n:
		s+=i
	return s
print(f4(5,5))

#Keyword with arg:
def f5(**kwvar):
	for k,v in kwvar.items():
		print('k:',k,'v:',v)
f5(x=40,a=10,b=30)
#Output
#k: x v: 40
#k: a v: 10
#k: b v: 30
