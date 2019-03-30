import urllib.request
import urllib.parse

url="https://www.naver.com"
mem=urllib.request.urlopen(url).read()
#print(mem)
print(mem.decode('utf-8'))



#https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%B4%88%EC%BD%94
#?전까지 를 복사 해서 api에 넣음
api="https://search.naver.com/search.naver"
values={
    'sm':'top_hty',
    'fbm':'0',
    'ie':'utf8',
    'query':'초코'
}

params=urllib.parse.urlencode(values)
url=api+'?'+params
data=urllib.request.urlopen(url).read()
text=data.decode('utg-8')
print(text)