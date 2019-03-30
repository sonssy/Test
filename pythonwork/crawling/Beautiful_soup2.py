from bs4 import BeautifulSoup
import urllib.request, time
'''
url="https://finance.naver.com/marketindex/"
response = urllib.request.urlopen(url)#url넣어주기

soup=BeautifulSoup(response,'html.parser')
results=soup.select('span.value')#값이 리스트로 나오기떄문에 for문으로 뽑아냄
for result in results[:3]:#리스트 중 인덱스0~2까지 만 값을 받음
    print(result.string)
    
print('원달러환율: ', results[0].string)
print('원달러환율: ', results[1].string)
print('원달러환율: ', results[2].string)

url1="https://finance.naver.com/sise/"
response1 = urllib.request.urlopen(url1)

soup1=BeautifulSoup(response1,'html.parser')
results1=soup1.select('span#KOSPI_now')#값이 리스트로 나오기떄문에 for문으로 뽑아냄
for result1 in results1:#리스트 중 인덱스0~2까지 만 값을 받음
    print(result1.string)



url2="http://www.cgv.co.kr/movies/"
response2 = urllib.request.urlopen(url2)

soup2=BeautifulSoup(response2,'html.parser')
results2=soup2.select('strong.title')
for result2 in results2:
    print("상영중: "+result2.string)



url3="https://music.bugs.co.kr/chart/"
response3 = urllib.request.urlopen(url3)

soup3=BeautifulSoup(response3,'html.parser')
results3=soup3.select('th p.title a')
for result3 in results3:
    print("제목: "+result3.string)


url4="https://www.naver.com/"
response4 = urllib.request.urlopen(url4)

soup=BeautifulSoup(response4,'html.parser')
keywords = soup.find_all('span',class_='ah_k')#span태그 및의 class찾을떄 _ 도 붙여줘야됨
#for 뒤쪽을 먼저하고 for 앞쪽의 형식으로 값을 받음
keywords = [each_line.get_text().strip() for each_line in keywords[:20]]#strip은 공백제거,get_text는 데이터에서 문자열만 추출
print(keywords)


url4="https://news.naver.com/"
response4 = urllib.request.urlopen(url4)

soup=BeautifulSoup(response4,'html.parser')
keywords=soup.select('ul.section_list_ranking li a')

slist = []

for each_line in keywords[:10]:#strip은 공백제거,get_text는 데이터에서 문자열만 추출
    #print(each_line.get('href'))
    slist.append(each_line.get('href'))
    #print(slist)

for i in slist:
    url = "https://news.naver.com/"+i
    #중도포기......그냥 밑에꺼 보고 하셈

#연합기사 링크 타고 들어가서 크롤링 
url="https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
results=soup.select('.section_list_ranking li a')
for result in results:
    #print('제목:', result.attrs['title'])#속성중 타이틀 값 가져옴
    #print('링크:', result.attrs['href'])#속성중 gref 가져옴
    #print()
    url_content='https://news.naver.com/'+result.attrs['href']
    response_content = urllib.request.urlopen(url_content)
    soup_content=BeautifulSoup(response_content,'html.parser')
    content=soup_content.select_one('#articleBodyContents')
    
    #print(content.contents)
    time.sleep(10)
#가공작업
    output=""
    for item in content.contents:
        stripped=str(item).strip()#문자열로 바꿔서 공백을 다 없앰>>줄바꿈태그등이 다 없어짐
        if stripped == '':
            continue
        if stripped[0] not in['<','/']:#태그나 주석제거
            output+=str(item).strip()
    print(output.replace('본문 내용tv플레이어',''))
    print()
    time.sleep(10)
    
'''