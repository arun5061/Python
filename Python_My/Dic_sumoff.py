dic=eval(input("Enter dict to find sum:"))
x=([(4,5)])
dic.update(x)
print(dic)
s=sum(dic.values())
sum=0
print('S:',s)
for k in dic.values():
    sum=sum+k
print('sum of:',sum)
