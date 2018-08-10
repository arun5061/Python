import sqlite3
import re
con = sqlite3.connect('test.db')
c = con.cursor()
c.execute("drop table stu")
q1="create table stu (sno INT, sname TEXT, smark INT)"
c.execute(q1)
q2="insert into stu values(121, 'Arun', 85)"
q3="insert into stu values(143, 'sunny',50)"
q4="insert into stu values(120, 'dunny',89)"
c.execute(q2)
c.execute(q3)
c.execute(q4)
con.commit()
print('Insert done')
c.execute("select * from stu")
d1=c.fetchall()
print('d1:',d1)
mar=int(input("Enter marks:"))
q5="update stu set smark=%d where sname='Arun'"
c.execute(q5 %mar)
con.commit()
c.execute("select * from stu")
d2=c.fetchall()
print('d2:',d2)
q6="delete from stu where sname='dunny'"
c.execute(q6)
con.commit()
c.execute("select * from stu")
d3=c.fetchone()
print('d3:',d3)
while d3 is not None:
	f=open('studata1.txt', 'a')
	f.write(str(d3)+',')
	d3=c.fetchone()
f.close()
rf=open('studata1.txt', 'r')
r=rf.read()
print(r)
w=r.replace('(', "")
x=w.replace(')', "")
y=x.strip()
print(x)
l=re.split('[,]+', y)
print(l)
rf.close()
