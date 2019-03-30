#zip
print(list(zip(['kor','eng','mat'],[40,30,70])))

print('=================================================')

#json
import json
student={'id':2002345,'name':'홍길동','history':[{'date':'20018-03-11','lang':'java'},{'date':'2019-07-23','lang':'python'}]}

jsonString=json.dumps(student,ensure_ascii=False,indent=4)#파이썬파일을 제이슨으로
print(jsonString)
print(type(jsonString))

print('=================================================')

import json
with open('jsonTest/data.json',encoding='UTF8')as f: #제이슨파일을 파이썬으로
    data=json.load(f)
print(type(data))
print(data)