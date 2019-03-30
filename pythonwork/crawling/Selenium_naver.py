from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time, sys
driver = wd.Chrome(executable_path='./crawling/data/chromedriver')
driver.implicitly_wait(3) # 3초기다리는거

'''
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('ukyo153')#값 입력하기
driver.find_element_by_name('pw').send_keys('암호')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(20)
'''
'''
id="ukyo153"
pw="암호"

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")#\넣는이유>>따옴표를 문자의 용도로 쓰기위해
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[2]/a').click()
time.sleep(1)

driver.get('https://mail.naver.com/?n=1553324865504&v=f')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results1=soup.select('strong.mail_title')
for result1 in results1:
    print(result1.string)
'''
driver.get('http://211.110.165.201:8080/ssy/member_login.do')
driver.find_element_by_name('mem_email').send_keys('c')
driver.find_element_by_name('mem_pw').send_keys('c')
driver.find_element_by_class_name('btn-primary').click()
time.sleep(1)
driver.get('http://211.110.165.201:8080/ssy/spotmain.do')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results1=soup.select('h2.display-5')
for result1 in results1:
    print(result1.string)



driver.close()
driver.quit()
sys.exit()