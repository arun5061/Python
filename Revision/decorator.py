#Function decorators
def deco(f):
	def inner(name):
		if name=='kumar':
			print('Hellooo',name,'Bad morning')
		else:
			return f(name)
	return inner
@deco
def f(name):
	print('Hellooo',name,'Good morning')

f('Arun')
f('kumar')
