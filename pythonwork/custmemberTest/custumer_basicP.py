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
        for index, each in enumerate(custlist):
            if each['email']==delmember:
                check=1
                del custlist[index]
                print(custlist)
            
            elif check==0:
                print('없는 이메일')
                break         
      

    elif choice=="U": 
        print("고객 정보 수정")
        updatemem=str(input('수정할 이메일입력'))
        check=0
        for index, each in enumerate(custlist):
            if each['email']==updatemem:
                check=1
                print(index, each)
                x=str(input('변경할 항목 선택'))
                y=str(input('변경값입력'))
                each[x]=y
                print(each)
            elif check==0:
                print('없는 이메일')
                break
    elif choice=="Q":
        print("프로그램 종료")
        break


