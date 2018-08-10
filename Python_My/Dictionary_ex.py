d=dict()
print(d)
#Multiple values:
d={100:'Arun',200:['vishnu','kiran']}
print(d[100])
print(d[200])
print(d)

#Dictionary example:
stu={}
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter name:")
    marks=int(input("Enter marks in %:"))
    stu[name]=marks
print(stu)
while True:
    name=input("Enter students name:")
    sub_marks=stu.get(name,-1)
    if sub_marks==-1:
        print('Student not found')
    else:
        print('Marks of student{}:{}'.format(name,sub_marks))
    option=input('Do you want to get one more student marks [Yes|No]:')
    if option=='No'or'no':
        break
print('Thanks for using my app')

