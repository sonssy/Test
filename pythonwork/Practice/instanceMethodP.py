class CircleCalculator(object):
    __PI=3.14
    @classmethod
    def calculate_area(cls,radius):
        area=cls.__PI*(radius**2)
        return round(area,2)
    
    @classmethod
    def calculate_circumference(cls,radius):
        circumference=2*cls.__PI*radius
        return round(circumference,2)

if __name__=='__main__':
    print('반지름:',3,"면적:",CircleCalculator.calculate_area(3))
    print('반지름:',3,"둘레:",CircleCalculator.calculate_circumference(3))

#__언더바 두개는 숨김이지만 클래스 매소드는 자기자신의 주소이기떄문에 불러서 사용가능함ex)cls.__PI
print('----------------------------------')

class CircleCalculator1(object):

    @staticmethod
    def calculate_area(radius,pi):
        area=pi*(radius**2)
        return round(area,2)
    
    @staticmethod
    def calculate_circumference(radius,pi):
        circumference=2*pi*radius
        return round(circumference,2)

if __name__=='__main__':
    print('반지름:',3,"면적:",CircleCalculator1.calculate_area(3,3.14))
    print('반지름:',3,"둘레:",CircleCalculator1.calculate_circumference(3,3.14))

