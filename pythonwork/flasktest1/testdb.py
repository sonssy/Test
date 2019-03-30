import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',password='qwer1324',database='test',port=3306)
print(conn)
conn.close()