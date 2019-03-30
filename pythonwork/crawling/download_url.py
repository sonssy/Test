import urllib.request
import os

#예시
'''
with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(300))#300바이트'''

#이미지주소
url='http://notefolio.net/data/img/17/e3/17e3405d7482250cacc3751b9e12c7e19e858de382d8ac6a132e6cf605a75a0b_v1.jpg'

#실행하는 파일의 경로를 찾아서 같은 경로에 이미지저장
dirname=os.path.dirname(__file__)#현재 파일의 위치
print(dirname)
savename=dirname+'/test.png'

#파일로 저장
#urllib.request.urlretrieve(url,savename)

#파일을 열고...활용할수있다
mem = urllib.request.urlopen(url).read()#정보 읽을떈는 read 함수이용
print(urllib.request.urlopen(url))

#위에서불러온파일을 저장함.
with open(savename,mode='wb') as f:#open 함수를 이용해서 (불러올 파일과 모드설정(wb 쓰기))
    f.write(mem)
    print('저장되었습니다.')
