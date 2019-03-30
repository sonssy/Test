def hap(x,y):
    return(x+y)

print(hap(10,20))
print((lambda x,y:x+y)(10,40))

print('--------------------------------------')

pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
def shortKey(pair):
    return pair[1]

pairs.sort(key=shortKey)
print(pairs)

pairs.sort(key=lambda pair:pair[0])
print(pairs)

print('--------------------------------------')

def make_increment(n):
    print("n",n)
    return lambda x:x+n

f=make_increment(42)

print(make_increment(0))
print(f)
print(f(0))

print(f(1))

print(make_increment(65)(1))

print('--------------------------------------')

#람다와 필터같이 쓰기

arr=[1,2,3,4,5,6,7,8,9]
brr=list(filter(lambda x:x%3==0,arr))
print(brr)

for item in brr:
    print(item,end=" ")

