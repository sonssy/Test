import sqlite3
conn=sqlite3.connect('./sqlliteTest/example.db')
c=conn.cursor()

#Create table (text=varchar, float=real)
c.execute('''CREATE TABLE if not exists stocks (date text, trans text, symbol text, qty real, price real)
''')

#Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2019-03-17)','BUY','RHAT',100,35.14)")
#Save (commit) the changes
conn.commit()

conn.close()