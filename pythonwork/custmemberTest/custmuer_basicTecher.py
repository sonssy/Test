import re
custlist=[]
page=-1


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

    
    if choice=="I":
        customer={'name':'','email':'','sex':'','birth':''}
        customer['name']=str(input('이름입력'))

        while True:
            customer['sex']=str(input('M OR F'))
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
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
            customer['birth']=str(input('출생년도 4자리수로 입력'))
            if len(customer['birth']) == 4:
                int(customer['birth'])
                break
        print(customer)
        custlist.append(customer)
        print(custlist)
        page +=1

        
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page>=0:
            print('현재페이지는 {}쪽입니다.'.format(page + 1))
            print(custlist[page])
        else:
            print('입력된 정보가 없습니다.')
    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page<=0:
            print('첫번째 페이지이므로 불가')
            print(custlist[page])
        else:
            page -=1
            print('현재페이지는 {}쪽입니다.'.format(page + 1))
            print(custlist[page])

    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page>=len(page)-1:
            print('마지막 페이지이므로 불가')
            print(custlist[page])
        else:
            page +=1
            print('현재페이지는 {}쪽입니다.'.format(page + 1))
            print(custlist[page])

    
    elif choice=='D':
        print("고객 정보 삭제")
        delmember=str(input('삭제할 이메일입력'))
        check=0
        for i in range(0,len(custlist)):
            while custlist[i]['email']==delmember:
                print('{}고객님의 정보가 삭제되었습니다.'.format(custlist[i]['email']))
                check=1
                del custlist[i]
                print(custlist)
                break
            if check==1:
                break
        if check==0:
            print('등록되지않은 이메일입니다.')

    elif choice=="U":
        while True:
            choice1=input('수정하시려는 고객정보의 이메일을 입력하세요: ')
            idx=-1
            for i in range(0,len(custlist)):
                if custlist[i]['email']==choice1:
                    idx=i
            if idx==-1:
                print('등록되지않은 이메일')
                break

            choice2=input('name,sex,birth 중 고르시오 : ')
            if choice2 in ('name','sex','birth'):
                custlist[idx][choice2]=input('수정할{}입력'.format(choice2))
                break
            elif choice2 == 'exit':
                break
            else:
                print('존재하지않는 정보')
                break       
    elif choice=="Q":
        print("프로그램 종료")
        break

