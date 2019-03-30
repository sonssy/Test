from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name="son")


@app.route('/plist')
def plist():
    list = {"motor","pir","servor","sound","door"} # <= 셋 키값이 없고 순서도 없지만 중복된갑은 안됨
    return render_template("plist.html",plist=list)

@app.route('/ulist')
def ulist():
    list={"led1":"ON","led2":"OFF","led3":"ON","temp":32,"motor":90,}
    return render_template("list.html",ulist=list)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)#기본 포트는 80 이라서 안적어도됨