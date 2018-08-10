from threading import*
def display():
	print('This code is executed by thread:',current_thread().getName())
display()
t=Thread(target=display)
t.start()

