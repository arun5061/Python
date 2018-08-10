def dec(f):
	def inn(a,b):
		if b==0:
			return ("can't div")
		else:
			return f(a,b)
	return inn
def f(a,b):
	return a/b
divfun=dec(f)
print(divfun(10,0))
print(f(10,0))