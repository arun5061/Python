import os,shutil
sorc=r'C:\Users\Nettyam Arun Kumar\Desktop\Test\Sorc'
os.makedirs(r'C:\Users\Nettyam Arun Kumar\Desktop\Test\Dest')
dest=r'C:\Users\Nettyam Arun Kumar\Desktop\Test\Dest'
for f in os.listdir(sorc):
	x=os.path.join(sorc,f)
	if x.endswith('.txt'):
		shutil.move(x,dest)
	else:
		os.remove(x)
os.rmdir(r'C:\Users\Nettyam Arun Kumar\Desktop\Test\Sorc')
#shutil.rmtree('dir') --> This will remove entire dir and it's content's