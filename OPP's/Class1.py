class c1:
	def __init__(self,fName,lName):
		self.fName=fName
		self.lName=lName
		self.sId='121FA05061'
		print('1:',self.fName+self.lName)
	def display(self):
		print('2:',self.fName+self.lName)
		self.f1()
	def f1(self):
		print('hi')
	@classmethod
	def sinfo(cls,n1,n2):
		return c1(n1,n2)

t=c1.sinfo('Arun','Kumar')
print(t.fName)
