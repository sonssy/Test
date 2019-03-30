import pymysql


conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql='''insert into users values('hong3','1234','홍길동1',501,'k1oea@qf.ccc','한국 그 어딘가에1','woman','010-8282-8282'); '''
        cursor.execute(sql)
        conn.commit()
    
    with conn.cursor() as cursor:
        sql='''select * from users'''
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        
finally:
    conn.close()