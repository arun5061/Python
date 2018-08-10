from random import *
t=('a','b','c','arun','sunny','bunny',1,2,3)
for i in range(1):
    print(random())#--->This will give values in between 0 and 1,0<x<1 exclusive of 0 and 1
    print(randint(1,15))#-->This will give any values from x to y, inclusive of 1,15
    print(uniform(1,15))#--> Exclusive of x,y, returns float values in between
    print(randrange(10,100,5))#--> start<=x<stop with step, inclusive of start and exclusive of stop
    print(choice(t))#--> Random value from list
    print('OTP:')
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
    print('seq of alpha and digit')
    print(chr(randint(97,97+25)),randint(0,9),chr(randint(97,97+25)),randint(0,9),chr(randint(97,97+25)),randint(0,9),sep='')
