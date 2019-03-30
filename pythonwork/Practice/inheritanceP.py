#상속
#부모격인 my클래스를 sunmy에서 (my)로 부모로 my를 쓰겟다고 받아서 사용함
#print 쓸떄 sunmy에 없으면 부모에서 찾아서 씀

class My:
    def __init__(self):
        self._name='korea'
        print('My')
    def get_name(self):
        print('self._name',self._name)
        return self._name

class SunMy(My):
    def __init__(self):
        super().__init__()
        print("SunMy")
    def sub_print(self):
        print('sub_print',self.get_name())

s=SunMy()
print(s._name)
print('메소드',s.get_name())
print('----------------------------------------')
s.sub_print()

print('=============================================================================')


class Car(object):
    def __init__(self):
        self._speed=0
    
    @property
    def speed(self):
        return self._speed
    def start(self):
        self._speed=20
    def accelerate(self):
        self._speed=self._speed+30
    def stop(self):
        self._speed=0

class SportCar(Car):
    def __init__(self):
        super().__init__()
        self._color='red'
    def accelerate(self):
        self._speed=self._speed+40
    def turbocharge(self):
        self._speed=self._speed+70
    @property
    def color(self):
        return self._color

if __name__=="__main__":
    my_sportcar=SportCar()
    print('색상:',my_sportcar.color)
    my_sportcar.start()
    print('속도:',my_sportcar.speed)
    my_sportcar.accelerate()
    print('속도:',my_sportcar.speed)
    my_sportcar.turbocharge()
    print('속도:',my_sportcar.speed)
    my_sportcar.stop()
    print('속도:',my_sportcar.speed)