import pickle,Emp
f=open('emp.txt','wb')
n=int(input('Enter number of records:'))
for i in range(n):
    eno=int(input('Enter eno:'))
    ename=input('Enter ename:')
    eadd=input('Enter eadd:')
    e=Emp.emp(eno,ename,eadd)
    e.display()
    pickle.dump(e,f)
    print("completed pickling..")
f.close()
