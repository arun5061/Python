import os,re
os.chdir(r"C:\Users\Nettyam Arun Kumar\Desktop\Test")
for f in os.listdir():
	f_name, f_title=os.path.splitext(f)
	os.rename(f,f_name)

