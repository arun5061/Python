#Srting Index:

s=input("Enter string:")
i=0
for x in s:
    print("String at +ve index:{}, String at -ve index:{}, present value of s:{}".format(i,i-len(s),x))
    i+=1
x=len(s)-1
for j in range(1,len(s)+1):
    print(s[-j],end='') #- Negative indexing
    print(s[x])  #- Positive indexing
    x-=1
sub=input("Enter sub string:")
if sub in s:
    print(sub,": present in main string")
else:
    print(sub,": not present in main string")

count=0
for k in range(len(s)):
    if count<=2:
        print(s[k],end='')

        
    
    
    
