import re
pattern=re.compile('python')
matcher=pattern.finditer('python is very easy language python')
for m in matcher:
	print('1)',m.start(),m.end(),m.group())
print('........................')
match=re.finditer('(ab)?','abbabbabaab')
for i in match:
	print('2)',i.start(),i.end(),i.group())
print('.................')

match=re.finditer('[a-z]','ab%&44343b aab')
for i in match:
	print('3)',i.start(),i.end(),i.group())

t=re.subn('a{3}','xxxxx','aaaaabbbnnfefefeaaaakdsds')
print('subn:',t)

x='015558866146'
s=re.sub('\d','xxx',x)
print(s)
r=x.replace(x[2:3],'x')
print(r)

s=input('To validate mob num:')
m=re.fullmatch('(0|91|\+91)?[6-9]\d{9}',s)
if m!=None:
	print('Valid num')
else:
	print('Not a valid num')





