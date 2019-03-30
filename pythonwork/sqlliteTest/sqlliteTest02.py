import sqlite3
conn=sqlite3.connect('./sqlliteTest/example.db')
c=conn.cursor()
'''
t=("RHAT",)
sql='SELECT * FROM stocks WHERE symbol=?'
c.execute(sql, t)#?에 해당하는거를 sql, 뒤쪽으로 쭉 붙여주면됨
print(c.fetchone())#one은 하나만

purchases=[('2019-03-10','BUY','IBM',1000,45.00),
           ('2019-03-11','BUY','IBM',1000,75.00),
           ('2019-03-12','SELL','IBM',1000,15.00),
           ('2019-03-14','BUY','MSFT',1000,55.00)]

c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)',purchases)#여러개 넣을때 batch
conn.commit()
'''
c.execute('select * from stocks ORDER BY price')
rows=c.fetchall()
for row in rows:
    print(row)

conn.close()