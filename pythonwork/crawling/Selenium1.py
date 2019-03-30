from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time, sys
driver = wd.Chrome(executable_path='./crawling/data/chromedriver')

'''
url='http://www.naver.com'
driver.get(url)
time.sleep(20)
driver.close()
driver.quit()

############

#youtube 동영상 필터값
filters={
    'hour':'EgQIARAB',#지난한시간
    'today':'EgQIAhAB',
    'week':'EgQIAxAB',
    'month':'EgQIBBAB',
    'year':'EgQIBRAB'
}

word = 'BTS'
url='https://www.youtube.com/results?search_query={word}&sp={date}'.format(word=word,date=filters['today'])
driver.get(url) #화면보여줌
time.sleep(3) #3초간 보여줌
html = driver.page_source #페이지 소스값 받아내는거
soup = BeautifulSoup(html,'html.parser')
title = soup.select('h3 > a#video-title')
print(title)

driver.close()
driver.quit()
sys.exit()


###############
'''

word = 'aa'
url='https://music.bugs.co.kr/search/integrated?q={word}'.format(word=word)
driver.get(url) #화면보여줌
time.sleep(3) #3초간 보여줌
html = driver.page_source #페이지 소스값 받아내는거
soup = BeautifulSoup(html,'html.parser')
titles = soup.select('p.title > a')
for title in titles:#리스트 중 인덱스0~2까지 만 값을 받음
    print(title.string)


driver.close()
driver.quit()
sys.exit()