
import re
custlist=[]
page = -1

def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            curSearch()
        
        elif choice=='P':
            preSearch()

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            quit()

def insertData():        
    customer={'name':'','sex':'',"email":'',"birthyear":''}
    while True:
        customer['name']=str(input("이름을 입력하세요 : "))
        if len(customer['name'])<=30:
            break
        else:
            print('30자 이내로 입력해주세요')
        
    while True:
            customer['sex']=str(input("성별(M/m 또는 F/f)을 입력하세요 : "))
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
            else:
                print('M/m 또는 F/f 중 입력해주세요')

    while True:
            customer['email']=str(input('이메일입력'))
            check=0
            for i in custlist:
                if i['email']==customer['email']:
                    check=1
                    #정규식 이용
                    emailreg = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.]$[a-zA-Z]{2,3}')
                    golbang=emailreg.search(customer['email'])
                    if golbang != None:
                        break
                    else:
                        print('@를 포함한 정확한 이메일입력')
            if check==0:
                break
            print('중복된 이메일')       

            

    while True:
            customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")    

            try: #인트값으로 바꿀수있게 제대로 들어왔는가
                int(customer['birthyear'])
            except: #인트값으로 변환불가
                print('숫자를 입력해주세요')
            else: #인트값으로 변환가능하면
                if len(customer['birthyear'])==4:
                    break
                else:
                    print('4자리로 입력해주세요')

    print(customer)
    custlist.append(customer)
    print(custlist)
    global page
    page += 1
    
def curSearch():
    print("현재 페이지는 {}쪽 입니다".format(page + 1)) 
    print(custlist[page])

def preSearch():
    global page
    if page <= 0:
        print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
        print(custlist[page])
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
        
def nextSearch():
    global page
    if page >= len(custlist)-1:
        print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
        print(custlist[page])
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])

def deleteData():
    choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)):
        while custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            delok = 1
            break
        
        if delok == 1:
            break

    if delok == 0:
            print('등록되지 않은 이메일입니다.')

def updateData(): 
    while True:
        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ')
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
        if idx==-1:
            print('등록되지 않은 이메일입니다.')       
            break
                    
        choice2=input('''
        다음 중 수정하실 정보를 골라주세요 
                name, sex, birthyear
        (수정할 정보가 없으면 'exit' 입력)
        ''')
        if choice2 in ('name','sex','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break
 
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  
    exe(choice)