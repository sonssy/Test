class CAr:
    def __init__(self):
        self.price=2000
        self._speed=0
        self.__color='red'

if __name__=='__main__':
    my_car=CAr()
    print(my_car.price)
    print(my_car._speed)
    #print(my_car.__color)
    print(dir(my_car))
    print(my_car._CAr__color)

#밑줄 __ 두개 인거는 안보임, 접근불가이므로 에러발생
#dir 로 찾아서 바뀐 이름으로 접근은 가능함