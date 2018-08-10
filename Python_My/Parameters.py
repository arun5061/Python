#Fun1:
def fun1(a,b,*n):
    print('hi')
    pass
fun1(10,20,300,400,500)

#Positional parameters:
def f1(a,b,c):
    pass
f1(10,20,30)

#Keyword parameters:
def f2(a,b,c):
    pass
f2(c=30,a=20,b=50)

#default parametrs --> This should at last argument value
def f3(b,c,a='hello'):
    print('b:',b,'c:',c,'a:',a)
f3(10,20)
#Varaiable lenth arguments:
def f4(a=10,*n):
    print('-------')
    print(n,a)
    for i in n:
        print(i)
f4()
f4(1000,10)
f4(20,30)
f4(40,50,60)

def f5(**k):
    for k,v in k.items():
        print(k,'-----',v)
f5(name='Arun',Edu=10)
f5(school="Montessori",Hob="Time pass")


        

