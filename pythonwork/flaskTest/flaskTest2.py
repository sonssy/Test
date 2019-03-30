from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/cakes')#127.0.0.1/cakes
def cakes():
    return 'Yummy cakes!'


@app.route('/method/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User%s'%username #%s 포맷 문자열 %~~~문자열로 넣겠다

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username,age):
    return 'User%s,나이%d'%(username,age) #%s 포맷 문자열 %~~~문자열로 넣겠다,%d 는 숫자


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=80) #debug false 일떄는 실행후 바뀌는내용에대해서 적용안됨 내렸다가 다시해야됨 True는 바뀐내용 적용되지만 전부는안됨
    #host 0.0.0.0 은 외부에서도 접근가능
