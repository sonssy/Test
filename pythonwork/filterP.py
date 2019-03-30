
#filter 사용 값이 true 인것만 걸러서 보여줌

def isodd(x):
    if x%2==0:
        return False
    else:
        return True

listdata=[1,2,3,4,5,6,7,9,8,10]
print(list(filter(isodd,listdata)))

print('--------------------------------------------------')

def ff(i):
    if type(i)==int:
        return True
    else:
        return False

listdata1=['a',2,4,5,'t','d']
print(list(filter(ff,listdata1)))

print('=========================================================')

#sorted 함수

names={'mary':10999,'same':2111,'aimy':9778,'tom':20245,'michale':27115,'bob':5887,'kelly':7855}
ret1=sorted(names)
print(ret1)

def f1(x):
    return x[0]
def f2(x):
    return x[1]

ret2=sorted(names.items(),key=f1)
print(ret2)
ret3=sorted(names.items(),key=f2)
print(ret3)


print('--------------------------------------------------')

