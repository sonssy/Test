from flask import Flask

app=Flask(__name__)

@app.route('/') #기본페이지설정 ~~주소~~/ 이렇게 들어온것

def index():
    return 'hello world'

if __name__=='__main__':
    app.run() #실행