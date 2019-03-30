class preson1:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name=value
    @property
    def age(self):
        return self._age
    @age.setter
    def speed(self, value):
        self._age=value

p1=preson1('홍길동',20)
print(p1.name)
p1.name='가나다'
print(p1.name)

#함수 불러오듯 () 넣지않고 변수 처럼 사용하도록 되어있음

print('-------------------------------------------------')
#이 밑부분은 잘모르겟음
class person2:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def getName(self):
        print('get name')
        return self._name
    def setName(self,name):
        if name=='가나다':
            print('{}이름은 변경불가')
            return
        print('set name',name)
        self._name=name

#name=property(getName,setName)

p2=person2('홍길동',20)
print(p2.name)
p2.name='가나다'
print(p2.name)
