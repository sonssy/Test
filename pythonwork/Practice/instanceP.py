class STest:
    age=10
s1=STest()
s2=STest()
s1.age=30
s2.age=50

s2.gender='남'

print(s2.gender)    #클래스 생성이후에도 젠더는 없지만 필요하면 추가할수있음
#print(s1.gender)   #젠더가 없기떄문에 안나옴
print(s1.age)
print(s2.age)
print(STest.age)

print('----------------------------------------------')

class Circle(object):  #object 는 귣이 안적어도됨
    pi=3.14
    def __init__(self,radius):
        self._radius=radius
    @property
    def radius(self):
        return self._radius
    def get_area(self):
        area=Circle.pi*(self._radius**2)
        return round(area,2)
    def get_circumference(self):
        circumference=2*Circle.pi*self._radius
        return round(circumference,2)
    
if __name__=="__main__":
    circle1=Circle(3)
    print('원주률:',Circle.pi)
    print('반지름:',circle1.radius,'면적:',circle1.get_area())
    print('반지름:',circle1.radius,'둘레:',circle1.get_circumference())
    circle2=Circle(4)
    print('반지름:',circle2.radius,'면적:',circle2.get_area())
    print('반지름:',circle2.radius,'둘레:',circle2.get_circumference())