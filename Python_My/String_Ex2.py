#To print non-repeative elements
s=input("Enter string:")
for i in range(len(s)):
    if s[i] in s[i+1:len(s)]:
        pass
    else:
        print(s[i],end='')
print()
#To find sub string in main string - It will give index of the substring, we cxan pass attributes from starting pos to end pos
sub=input('Enter sub-strng:')
if s.find(sub) == -1:
    pass
else:
    print('find:',s.find(sub,4,10))

#Counting number of substings in main string
print("Count:",s.count(sub))
#print("Count:",s.count(sub,4,8))
print()

#Replacing old string with new string:
s1=s.replace('difficult',sub)
print(s1)
print()

#Splitting of string:
l=s.split(' ')
print(type(l))
for x in l:
    print(x)
print()

l=s.split(' ',2)
for x in l:
    print(x)
print()

r=s.rsplit(' ',2)
for x in r:
    print(x)

#To printeven or odd positions
    
for i in range(len(s)):
    if i%2==0:
        print("At even pos s[{}]={}".format(i,s[i]))
print()

for j in range(len(s)):
    if j%2!=0:
        print("At odd s[{}]={}".format(j,s[j]))

s1=s2=output=''

for y in s:
    if y.isalpha():
        s1=s1+y
    else:
        s2=s2+y
output=s1+s2
print('Output:',output)

newch=''
output=''
pre=''
for z in s:
    if z.isalpha():
        output=output+z
        pre=z
    else:
        newch=chr(ord(pre)+int(z))
        output=output+newch
print('Out2:',output)

  
    


        





