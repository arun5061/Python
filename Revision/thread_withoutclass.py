from threading import*
import time
class f1:
	def __init__(self):
		print('hi')
	def dis(self,a):
		# current_thread().setName('helloooo!')
		print('a:',a,'Hello your at:',current_thread().getName())
f=f1()
startTime=time.time()
t=Thread(target=f.dis, args=(10,))
t.start()
t.join()
endTime=time.time()
print('Hello your at:',current_thread().getName())
print('Time take:',endTime-startTime)
t2=f1().dis(150)