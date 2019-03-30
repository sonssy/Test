from bs4 import BeautifulSoup

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
#print(tag.name)#선택한 태크가 뭔지 보여줌
'''tag.name="blockquite"
print(tag.name)#태그이름도 조정가능

tag['id']
print(tag)

tag.attrs#모든 속성ㄷ르을 딕셔너리형태로 보여줌
print(tag.attrs)

tag['id'] = 'verybold'#id 값 바꾸기
tag['another-attribute'] = 1
tag

del tag['id'] #값 지우기
del tag['another-attribute']
tag

tag['id']

print(tag.get('id'))

print(tag.string)#안의 문자내용보기
print(soup.p.string)#p태그 안의 내용 보여줌
tag.string.replace_with("aaaaaaaaaaaaaaaaaaaaaa")#안의 내용 바꾸기
print(tag)

result=soup.find_all('a')#모든 a태그를 찾겠다>>여러개이기떄문에 리스ㅌ로 나옴
print(result)
print(result[1])#리스트이기떄무네 인덱스로 접근도 가능


body_tag=soup.body#바디 태그를 보여줌
print(body_tag)

body_tag1=soup.body.contents#바디 태그는 빠지고 그안의 태그안의 내용을 리스트로 보여줌
print(body_tag1)

for child in body_tag.children:
    print(child)

for child1 in body_tag.descendants:#하나하나 다 분리해서 보여줌
    print(child1)

for string in soup.strings:#\n 등의 띄어쓰기도 다 보ㅓ여줌
    print(repr(string))

for string1 in soup.stripped_strings:#띄어쓰기등 은 생략해서 보여줌
    print(repr(string1))#repr은 자바에서 toString 같은 거임

link = soup.a
for parent in link.parents:#parent s 부모클래스 모두다 보여줌
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        '''
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())#보기좋게 해줌
# <html>
#  <body>
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
#  </body>
# </html>
sbn=sibling_soup.b.next_sibling#형제찾기 나 다음의
# <c>text2</c>
print(sbn)
scp=sibling_soup.c.previous_sibling#형제찾기 나 이전의
# <b>text1</b>
print(scp)
print(sibling_soup.b.previous_sibling)
print(sibling_soup.c.next_sibling)

link = soup.a
print(link)
link.next_sibling

link.next_sibling.next_sibling

for sibling in soup.a.next_siblings: #s가 붙어서 여러개임 그래서 for문으로 뺴내야됨
    print(repr(sibling))