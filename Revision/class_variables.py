class emp:
	amt=0
	def __init__(self):
		emp.amt+=1
	def pay(self):
		print(self.amt)

e1=emp()
e2=emp()
e1.pay()
