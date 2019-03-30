import os
import sys
import urllib.request,json
import sqlite3
import pymysql
from flask import Flask,request,render_template,redirect,jsonify


list_records=[]


client_id = "ZuVEMvGVijkelodk3JiF"
client_secret = "9WGQJk0XY5"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/movie?query=" + encText+"&display=10" # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):#성공했을떄 200뜸
    response_body = response.read()
    titles=response_body.decode('utf-8')
    #print(titles)
    moviedict = json.loads(titles)#json을 dict으로 바꿔줌
    moviedict=moviedict['items']
    for h in moviedict:
        record=str(h['title'])
        record1=str(h['link'])
        record2=str(h['image'])
        record3=str(h['pubDate'])
        record4=str(h['director'])
        record5=str(h['userRating'])
        
        rec=tuple([record,record1,record2,record3,record4,record5])
        list_records.append(rec)
else:
    print("Error Code:" + rescode)


print(list_records)

conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

c=conn.cursor()

#마리아 db에 넣을댸는 ??가아니고 %s로 써야ㅚㅁ
sql="INSERT INTO movie_api(title,link,image,pubDate,director,rating) VALUES(%s,%s,%s,%s,%s,%s)"

c.executemany(sql, list_records)
#c.execute(sql)

conn.commit()

sql1='select * from movie_api'

c.execute(sql1)

rows=c.fetchall()
for row in rows:
    print(row)

conn.close()