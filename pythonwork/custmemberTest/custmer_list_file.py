import re,json

class customer:
    custlist=[]
    page = -1
    def firstinput(self):
        choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 고객 정보 입력
        C - 현재 고객 정보 조회
        P - 이전 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 고객 정보 수정
        D - 고객 정보 삭제
        S - 저장
        Q - 프로그램 종료
        ''')    
        return choice

    def insertData(self):
        
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
            customer['email']=input('이메일입력')
            check=0
            for i in self.custlist:
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
        self.custlist.append(customer)
        print(self.custlist)
        self.page += 1
        
    def curSearch(self):
        print("현재 페이지는 {}쪽 입니다".format(self.page + 1)) 
        print(self.custlist[self.page])

    def preSearch(self):
        
        if self.page <= 0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
            print(self.custlist[self.page])
        else:
            self.page -= 1
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            print(self.custlist[self.page])
            
    def nextSearch(self):
        
        if self.page >= len(self.custlist)-1:
            print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
            print(self.custlist[self.page])
        else:
            self.page += 1
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            print(self.custlist[self.page])

    def deleteData(self):
        self.custlist
        self.page
        choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
        delok = 0
        for i in range(0,len(self.custlist)):
            while self.custlist[i]['email'] == choice1:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(self.custlist[i]['name']))
                del self.custlist[i]
                print(self.custlist)
                delok = 1
                break
            
            if delok == 1:
                break

        if delok == 0:
                print('등록되지 않은 이메일입니다.')

    def updateData(self): 
        self.custlist
        self.page
        while True:
            choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ')
            idx=-1
            for i in range(0,len(self.custlist)):
                if self.custlist[i]['email'] == choice1:
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
                self.custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                break
            elif choice2 =='exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    def saveData(self):
        jsonString = json.dumps(self.custlist,ensure_ascii=False,indent=4)
        print(jsonString)
        fp=open('jsontest/data.json','wt',encoding='utf-8')
        fp.write(jsonString)

    
    def loadData(self):
        fp=open('jsontest/data.json','rt',encoding='utf-8')
        jsonString=fp.read()
        print(jsonString)
        self.custlist=json.loads(jsonString)

    def exe(self,choice):
        if choice=='I':
            self.insertData()
        
        elif choice=='C':
            self.curSearch()
        
        elif choice=='P':
            self.preSearch()

        elif choice=='N':
            self.nextSearch()

        elif choice=='U':
            self.updateData()
        
        elif choice=='D':
            self.deleteData()
        
        elif choice=='S':
            self.saveData()
                       
        elif choice=='Q':
            quit()
    def __init__(self): #생성자>>초기화같은거임>>맨처음해야할일들을 담아두는곳>>첫화면?정도
        self.loadData()
        while True:
            self.exe(self.firstinput())
    
  
customer()