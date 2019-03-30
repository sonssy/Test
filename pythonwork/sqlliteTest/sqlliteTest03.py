import sqlite3
from bs4 import BeautifulSoup
import urllib.request, time

conn=sqlite3.connect('./sqlliteTest/example.db')
c=conn.cursor()

#v페이지가 있는 사이트에서 가져오기
params=urllib.parse.urlencode({'page':1})
url="https://movie.naver.com/movie/point/af/list.nhn?&%s" %params
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response,'html.parser')
table=soup.find('table',class_='list_netizen')

list_records=[]
for i,r in enumerate(table.find_all('tr')):
    for j,c in  enumerate(r.find_all('td')):
        if j==0:
            record=int(c.text.strip())
        elif j==2:
            record1=int(c.text.strip())
        elif j==3:
            record2=str(c.find("a",class_='movie').text.strip())
            record3=str(c.text).strip('\n')[2]
        elif j==4:
            record4=c.find("a",class_='author').text.strip()
            record5=str(c.text).split('****')[1]
    try:
        rec=tuple([record,record1,record2,record3,record4,record5])
        list_records.append(rec)
    except:
        pass
print(list_records)

#Create table (text=varchar, float=real)
sql2='CREATE TABLE if not exists movie (no integer, grade integer, title text, content text, writer text, date text)'
c.execute(sql2)
'''

sql=('INSERT INTO movie VALUES(?,?,?,?,?,?)')

c.executemany(sql, list_records)

conn.commit()

sql1=('select * from movie')

c.execute(sql1)

rows=c.fetchall()
for row in rows:
    print(row)
'''
conn.close()