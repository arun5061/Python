import sqlite3
con = sqlite3.connect('test.db')
c = con.cursor()
if con:
	print('Connected')
else:
	print('Not connected')
c.close()
con.close()
