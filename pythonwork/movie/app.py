from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
#flask는 웹, request는 값전달,render_template는 html띄우기위함

app=Flask(__name__) #초기화해서 app에 주소값 넣음

#메인화면
@app.route('/moviemain')#주소임
def mainmovie():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='''select * from movie '''
            cursor.execute(sql)
            result=cursor.fetchall()

    finally:
        conn.close()
    return render_template('main.html',list=result)

#ajax검색
@app.route('/ajaxmain',methods=['POST'])#주소임
def searchmovie():
    text=request.form.get('text')
    stype=request.form.get('stype')
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            if stype == 'm_title':
                sql="select * from movie where m_title like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
            elif stype == 'm_act':
                sql="select * from movie where m_act like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
            else:
                sql="select * from movie where m_dir like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
    finally:
        conn.close()
        return jsonify(result)
    
    


#영화상세
@app.route('/movie_detail/<m_no>')#주소임
def detial(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='''select * from movie where m_no= %s;'''
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄

            sql='''select * from board where m_no= %s;'''
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()

        return render_template('movie_detail.html',list=result,board=board)
#영화등록
@app.route('/form', methods=['GET'])
def formTest():
    return render_template('form.html')#form.html을 호출하겟다
#영화등록
@app.route('/formresult', methods=['POST'])
def formresult():
    title = request.form.get('title') #request 로 값을 받음
    mdir = request.form.get('mdir') #get은 값이 하나
    act = request.form.getlist('act') #getlist는 그 이름으로 갑이 여러개일때
    grade = request.form.getlist('grade') 
    date = request.form.getlist('date') 
    content = request.form.get('content')
    img = request.files['img']
    dirname=os.path.dirname(__file__) + '/static/uploads/'+img.filename
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="insert into movie(m_title,m_dir,m_act,m_content,m_grade,m_img,m_date) values(%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql,(title,mdir,act,content,grade,img.filename,date))

            conn.commit()
    finally:
        img.save(dirname)
        conn.close()
    return redirect('/form')

#영화삭제하기
@app.route('/delete_movie/<m_no>',methods=['GET'])
def deleteform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="delete from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            conn.commit()
    finally:
        conn.close()

        return redirect('/moviemain')

#영화내용 수정하기
@app.route('/update_movie/<m_no>',methods=['GET'])
def updateform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="select * from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄
    finally:
        conn.close()

        return render_template('update_movie.html',list=result)
#영화수정
@app.route('/update_movie',methods=['POST'])
def updateformp():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    no = request.form.get('no') 
    title = request.form.get('title') 
    mdir = request.form.get('mdir') 
    act = request.form.getlist('act') 
    grade = request.form.getlist('grade') 
    date = request.form.getlist('date') 
    content = request.form.get('content')
    img = request.files['img']
    dirname=os.path.dirname(__file__) + '/static/uploads/'+img.filename

    try:
        with conn.cursor() as cursor:
            sql="update movie set m_title=%s,m_dir=%s,m_act=%s,m_content=%s,m_grade=%s,m_img=%s,m_date=%s where m_no=%s;"
            cursor.execute(sql,(title,mdir,act,content,grade,img.filename,date,no))
            conn.commit()
    finally:
        img.save(dirname)
        conn.close()
    return redirect('/moviemain')

#게시판글쓰기
@app.route('/board_write/<m_no>',methods=['GET'])
def boardW(m_no):
    return render_template('board_write.html',m_no=m_no)#form.html을 호출하겟다

@app.route('/board_write/<m_no>',methods=['POST'])
def boardP(m_no):
    title = request.form.get('title') 
    writer = request.form.get('writer') 
    content = request.form.get('content') 
    good = request.form.get('good') 
    m_no = request.form.get('m_no') 
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="insert into board(b_title,writer,b_content,good,m_no,b_date) values(%s,%s,%s,%s,%s,SYSDATE());"
            cursor.execute(sql,(title,writer,content,good,m_no))
            conn.commit()
    finally:
        conn.close()
    return redirect('/movie_detail/'+m_no)

#글내용
@app.route('/board_content/<b_no>',methods=['GET'])
def boardC(b_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='''select * from board where b_no = %s '''
            cursor.execute(sql,(b_no))
            result=cursor.fetchone()

    finally:
        conn.close()
    return render_template('board_content.html',list=result)

'''




#부트스트랩
@app.route('/bootstrap')
def bootstraptest():
    return render_template('bootstrap.html')


#한번에 name값 다 불러오기>>딕셔너리로 값이 옴
@app.route('/usersform',methods=['POST','GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')
    else:
        userid=request.form.get('userid')
        userpw=request.form.get('userpw')
        username=request.form.get('username')
        userage=request.form.get('userage')
        useremail=request.form.get('useremail')
        useradd=request.form.get('useradd')
        usergender=request.form.get('usergender')
        usertel=request.form.get('usertel')

        conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with conn.cursor() as cursor:
                sql="insert into users values(%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(sql,(userid,userpw,username,userage,useremail,useradd,usergender,usertel))
                conn.commit()
        finally:
            conn.close()
        return redirect('/list')
        
@app.route('/list',methods=['GET'])
def table():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql="select * from users"
            cursor.execute(sql)
            result=cursor.fetchall()# 다가져올떄
            
    finally:
        conn.close()
    return render_template('list.html',list=result)


@app.route('/updateform/<userid>',methods=['GET'])
def updateform(userid):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="select * from users where userid= %s;"
            cursor.execute(sql,(userid))
            result=cursor.fetchone() #하나만 가져올떄
    finally:
        conn.close()

        return render_template('updateform.html',list=result)
    
@app.route('/updateformp',methods=['POST'])
def updateformp():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    
    userid=request.form.get('userid')
    userpw=request.form.get('userpw')
    username=request.form.get('username')
    userage=request.form.get('userage')
    useremail=request.form.get('useremail')
    useradd=request.form.get('useradd')
    usergender=request.form.get('usergender')
    usertel=request.form.get('usertel')

        
    try:
        with conn.cursor() as cursor:
            sql="update users set userpw=%s,username=%s,userage=%s,useremail=%s,useradd=%s,usergender=%s,usertel=%s where userid=%s;"
            cursor.execute(sql,(userpw,username,userage,useremail,useradd,usergender,usertel,userid))
            conn.commit()
    finally:
        conn.close()
    return redirect('/list')
    
@app.route('/content/<userid>',methods=['GET'])
def content(userid):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="select * from users where userid= %s;"
            cursor.execute(sql,(userid))
            result=cursor.fetchone() #하나만 가져올떄
    finally:
        conn.close()

        return render_template('content.html',list=result)


@app.route('/deleteform/<userid>',methods=['GET'])
def deleteform(userid):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="delete from users where userid= %s;"
            cursor.execute(sql,(userid))
            conn.commit()
            
    finally:
        conn.close()

        return redirect('/list')


#이미지 가져오기
@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname=os.path.dirname(__file__)+'/static/img/'
    filenames=os.listdir(dirname)
    print(filenames)
    
    return render_template('imglist.html',list=filenames)


#ajax
@app.route('/ajaxlist',methods=['GET'])
def ajaxtable():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql="select * from users"
            cursor.execute(sql)
            result=cursor.fetchall()# 다가져올떄
    finally:
        conn.close()
        return render_template('ajaxlist.html',list=result)

@app.route('/ajaxlist',methods=['POST'])
def ajaxtableP():
    userid=request.form.get('userid')
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1324',db='member',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql="select * from users where userid like %s"
            userid=userid+'%'
            cursor.execute(sql,userid)
            result=cursor.fetchall()# 다가져올떄
            print(result)
    finally:
        conn.close()
        return jsonify(result)

#파일업로드
@app.route('/upload')
def uploadget():
    return render_template('uploadform.html')
#파일업로드처리
@app.route('/upload', methods=['POST'])
def uploadpost():
    f = request.files['uploadfile']#name 값받아옴
    #저장할경로+파일명
    dirname=os.path.dirname(__file__) + '/uploads/'+f.filename
    print(dirname)
    f.save(dirname)
    return 'uploads 디렉토리-> 파일업로드 성공!'

'''

if __name__=="__main__": #파일내에서만 직접적으로 동작하게끔
    app.run(host='0.0.0.0',port=80,debug=True)
#host0.0.0.0은 외부에서도 접근가능, port는 기본 5000으로 바꾸고 싶으면 바꾸면됨