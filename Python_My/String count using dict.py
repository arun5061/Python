word=input('Enter string:')
d={}
for k in word:
    d[k]=10
    print(';;;',d)
    d[k]=d.get(k,0)+1
print('d:',d)
for n,v in sorted(d.items()):
    print('{} occured {} times'.format(n,v))
    
d={}
s={'a','e','i','o','u'}
for k in word:
    if k in s:
        d[k]=d.get(k,0)+1
print('d:',d)
for n,v in sorted(d.items()):
    print('{} occured {} times'.format(n,v))
