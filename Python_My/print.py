a=input("Input Value:")
print("hi")
print() #An empty print can be used as a line seperator
print("HELLO \nGUD MRNG") #new line
print("HELLO \tGUD MRNG") #Tab space
print(3*3)
print("Dear","Arun")
print(1,2,3,4,'help',5,6,7,sep=' ') # Seperator between values
print(1,2,3,4,sep=':',end="...") #END - In between line seperator
print(6,7,8,9,sep='-')
#Formatted string:
a,b,c,d,e=10,20,'Arun',40.5,[10,20,15,'Mohan']
print(type(d))
print(type(e))
print("Hello you have entered %i,%i,'%s',%f,%s values" %(a,b,c,d,e))

#Replacment function
name='Vishnu'
height=5.11
bike='scooty'
print("hello {0} your height is {1} and bike type {2}".format(name,height,bike))
print("hello {} your height is {} and bike type {}".format(name,height,bike))
print("hello {x} your height is {z} and bike type {y}".format(x=name,z=height,y=bike))
