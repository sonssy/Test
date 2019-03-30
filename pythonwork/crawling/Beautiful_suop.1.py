from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,'html.parser')
#print(type(soup))
#print(soup.prettify())

tag=soup.a#.뒤에는 태크값
print(type(tag))
'''
#정규식도 가능 import re 햐야됨
for tag in soup.find_all(re.compile("^b")): #첫글자가 b 찾기
    print(tag.name)
# body
# b
for tag in soup.find_all(re.compile("t")):#t가 들어간거 전부 찾기
    print(tag.name)
# html
# title
'''
def has_class_but_no_id(tag):#함수정의>tag를 받아옴
    #class태그가 있고 id태그가 없는거만
    return tag.has_attr('class') and not tag.has_attr('id')


kk=soup.find_all(has_class_but_no_id)
#print(kk)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]

soup.find_all("title")#태그찾기
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")#태그여러개찾기

soup.find_all(id="link2")#아이디가 ~~인거

soup.find(string=re.compile("sisters"))#re는 정규식으로 sister가 들어있는거 찾기


soup.select("html head titile")#html 밑에 head밑에 있는 title
soup.select("head>title")#head 바로 밑에 있는데 head밑에 title이 바로 있어야됨
soup.select("p>a")#p태그 바로밑에 있는 a태그 p태그밑에 바로 a 태그있어야 나옴
ba=soup.select("body>a")
#print(ba)
ba1=soup.select("body a")#바디 밑에 바로 없어도 그냥 밑에 있으면 나옴
#print(ba1)

#아이디가 link1인거로 부터 뒤쪽으로 class가 sister인거 다~
ls=soup.select("#link1~.sister") ##은 아이디, . 은 클래스 리스트로 값나옴
print(ls)
#아이디가 link1인거 바로 뒤쪽으로 class가 sister인거 
ls1=soup.select("#link1+.sister")
print(ls1)
