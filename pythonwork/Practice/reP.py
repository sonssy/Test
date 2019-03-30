import re
data="""
park 800905-1049118
kim 700905-1059119
Lee 890603-2032072
"""
#^[] ^=시작,[^] ^=not
#{}=반복,- = ~~-!! ~~에서!!까지,[]=계속이어서
pat=re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

print('------------------------------------')

import re
p=re.compile('[a-z]+') #+=1~~, *=전부다
m=p.match("python")
print(m)

print('------------------------------------')

p=re.compile('[a-z]+') 
m=p.match("")
print(m)

print('------------------------------------')

p1=re.compile('ca*t')   #a전부
print(p1.match("ct"))
print(p1.match("cat"))
print(p1.match("caaaaaaat"))
print(p1.match("ca*t"))

print('------------------------------------')

p2=re.compile('ca+t')   #a가1개부터 무한대까지
print(p2.match("ct"))
print(p2.match("cat"))
print(p2.match("caaaaaaat"))
print(p2.match("ca+t"))

print('------------------------------------')

p3=re.compile('ca{2}t')  #a가2개인거만
print(p3.match("cat"))
print(p3.match("caat"))

print('------------------------------------')

p4=re.compile('ca{2,5}t') #a가{2,5}2~5
print(p4.match("cat"))
print(p4.match("caat"))
print(p4.match("caaat"))
print(p4.match("caaaaat"))
print(p4.match("caaaaaaaaaat"))

print('------------------------------------')

p5=re.compile('ab?c') #b 가 있어도되고 없어도 되는데 있다면 1번만
print(p5.match("ac"))
print(p5.match("abc"))
print(p5.match("abbc"))


print('------------------------------------')

p6=re.compile('^abc') #^abc abc가 앞쪽에 있는가
print(p6.search("abcqfq"))
print(p6.search("qabc"))
p7=re.compile('abc$') #abc$ abc가 맨뒤에 있는가
print(p7.search("werabc"))
print(p7.search("abcqq"))


print('------------------------------------')
#이메일등록 정규식
emailreg = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.]$[a-zA-Z]{2,3}')
#테스트해보면됨
print(emailreg.match('1qrfq11@naver.com'))
print(emailreg.match('awqrfq11naver.com'))
print(emailreg.match('awqrfq11@213aver.com'))
print(emailreg.match('awqrfq11@naver.comm'))
print(emailreg.search('awq11@naver.com'))


