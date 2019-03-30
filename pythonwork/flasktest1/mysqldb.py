import MySQLdb

#db 연결
db=MySQLdb.connect(host='127.0.0.1',user='root',password='qwer1324',database='test',port=3306)

cursor = db.cursor()#d얘가 커리문실행실킬꺼임

cursor.execute('SELECT VERSION()')#커리문받아서 실행

data= cursor.fetchone() #실행이 한줄일떄one 사용

print("Database version : %s" % data)#결과값 보여주기
#db 연결끊기
db.close()

