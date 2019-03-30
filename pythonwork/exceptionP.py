def get(key,dataset):
    try:
        value=dataset[key]
    except IndexError:
        return print('indexError')
    except KeyError:
        return print('KeyError')
    else:
        return value

print(get(3,(1,2,3)))
print(get('age',{'name':'홍길동','gender':True}))

print('------------------------------------------------------')

#BaseException 은 최상위 부모 이기떄문에 모든 예외를 다 잡음

def get1 (key,dataset):
    try:
        value=dataset[key]
    except BaseException:
        return None
    else:
        return value
            
print(get1(3,(1,2,3)))
print(get1('age',{'name':'홍길동','gender':True}))

print('------------------------------------------------------')

try:
    a=[1,2]
    print(a[3])
    4/0
    print("end")
except (ZeroDivisionError,IndexError) as e:
    print(e)

try:
    b=[1,2]
    print(b[1])
    4/0
    print("end")
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

print('------------------------------------------------------')

