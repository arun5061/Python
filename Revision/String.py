#Srting Index:
s='  Python is very difficult language'
print('Strip:',s.strip())
l=s.split()
print('Split:',l)
s1=s.replace('difficult','easy')
print('s1:',s1)
x='enjoy'
z=list(s+x)
print('z:',z)
print('find:',s.find('is',0,len(s)))
w=s.count('is',0,len(s))
print(w)
