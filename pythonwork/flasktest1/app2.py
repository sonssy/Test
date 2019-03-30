from flask import Flask,request,render_template,redirect,url_for
import pymysql,os
#flask는 웹, request는 값전달,render_template는 html띄우기위함

app=Flask(__name__) #초기화해서 app에 주소값 넣음


@app.route('/javas')#주소임
def index():
    return render_template('jstest.html')#index.html을 호출하겟다

    

if __name__=="__main__": #파일내에서만 직접적으로 동작하게끔
    app.run(host='0.0.0.0',port=80,debug=True)
#host0.0.0.0은 외부에서도 접근가능, port는 기본 5000으로 바꾸고 싶으면 바꾸면됨