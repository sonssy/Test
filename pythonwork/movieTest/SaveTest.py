#크롤링한 데이터를 파이썬 파일과 같은 위치에 result.json을 만들어 저장

from bs4 import BeautifulSoup
#urllib말고 requests로 불러 올꺼임
import requests
import json
import os

#파이썬 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))#abspath는 절대 경로

print(BASE_DIR)

req = requests.get('https://beomi.github.io/beomi.github.io_old/')#get방식으로 읽어옴
html=req.text
soup=BeautifulSoup(req,'html.parser')
my_titles=soup.select(
    'h3>a'
)
data={}

for title in my_titles:
    data[title.text]=title.get('href')
    #json파일로 저장
with open(os.path.join(BASE_DIR,'result_json'),'w+') as json_file:
    json.dump(data,json_file)


    