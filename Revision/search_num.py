import re
rf=open('num.txt','r')
af=open('numout.txt','w')
f_content=rf.readlines()
print(f_content)
for n in f_content:
	list=re.findall('[0|91|\+91]?[6-9]\d{9}',n)
	print('n:',n)
	for num in list:
		print('num:',num)
		af.write(num+'\n')
print('Extracted numbers')
rf.close()
af.close()
