import re
s='Arun-kumar.com'
l=re.split('[-.]',s)
print(l)
t=re.subn('\.com','.net',s)
print(t[0])
print(t[1])
