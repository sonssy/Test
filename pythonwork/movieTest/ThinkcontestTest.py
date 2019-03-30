from bs4 import BeautifulSoup
import urllib.request, time
import re

url="https://thinkcontest.com/Contest/CateField.html?c=12"
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')

#regex: .*(문자의 유형과 상관없이 그건이 반복되면 매칭), ?(그것이 있을숟 없을수도 있음)
#.*? (그것은 문자의 반복이지만 있을 ㅅ도 없을 수도 있다)
#re.DOTALL==.이 개행붐자를 포함한 모든문자를 의미하게됨
contests=soup.find_all('div',class_=re.compile("contest-title.*?",re.DOTALL))
keywords=[each_line.a.get_text().strip() for each_line in contests]
print(keywords)