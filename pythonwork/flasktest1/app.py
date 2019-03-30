from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
#flask는 웹, request는 값전달,render_template는 html띄우기위함

app=Flask(__name__) #초기화해서 app에 주소값 넣음


@app.route('/')#주소임
def index():
    return render_template('index.html')#index.html을 호출하겟다

@app.route('/form')#주소임
def formTest():
    return render_template('form.html')#form.html을 호출하겟다

@app.route('/formresult', methods=['POST'])
def formresult():
    userName = request.form['username'] #request 로 값을 받음
    userPass = request.form.get('userpass') #get은 값이 하나
    joblist = request.form.getlist('job') #getlist는 그 이름으로 갑이 여러개일때
    hobbylist = request.form.getlist('hobby') 
    chk_info = request.form.getlist('chk_info') 
    sex = request.form.get('sex')
    content = request.form.get('content')
    return render_template('formresult.html',username=userName,userpass=userPass,job=joblist,hobby=hobbylist,chk_info=chk_info,sex=sex,content=content)#값을 담아서 보냄

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
                sql='''insert into users values(%s,%s,%s,%s,%s,%s,%s,%s);'''
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
            sql='''select * from users'''
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
            
            sql='''select * from users where userid= %s;'''
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
            sql='''update users set userpw=%s,username=%s,userage=%s,useremail=%s,useradd=%s,usergender=%s,usertel=%s where userid=%s;'''
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
            
            sql='''select * from users where userid= %s;'''
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
            
            sql='''delete from users where userid= %s;'''
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
            sql='''select * from users'''
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
            sql='''select * from users where userid like %s'''
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



if __name__=="__main__": #파일내에서만 직접적으로 동작하게끔
    app.run(host='0.0.0.0',port=80,debug=True)
#host0.0.0.0은 외부에서도 접근가능, port는 기본 5000으로 바꾸고 싶으면 바꾸면됨