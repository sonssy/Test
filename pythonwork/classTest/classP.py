
class Car:
    _speed=0

    def get_speed(self):
        return self._speed

    def accelerate(self):
        self._speed+=10
    
car1=Car()
car1._speed=80
print(car1.get_speed())
car1.accelerate()
print(car1.get_speed())

print('---------------------------------------------')

class Sam(object):
    name='korea'
    def get_name(self):
        return self.name

    def gerinfo(self):
        self.get_name()

s1=Sam()
s2=Sam()
s3=Sam()

s3.name='japan'
print(s1.name)
print(s2.name)
print(s3.get_name())

print('---------------------------------------------')

class person:
    def __init__(self,name='홍길동',age=20):
        self._name=name
        self._age=age
        print(name,"객체생성")
    
    def showinfo(self):
        print(self._name,self._age)

s1=person()
s2=person('가나다')
s3=person(age=50)
s4=person("abcd",40)

s1.showinfo()
s2.showinfo()
s3.showinfo()
s4.showinfo()