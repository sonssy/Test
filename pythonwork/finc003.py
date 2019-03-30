

def circle_area_circumference(radius,pi):
    area=pi*(radius**2)
    circumference=2*pi*radius
    return area, circumference

if __name__=="__main__":
    result=circle_area_circumference(3,3.14)
    print('반지름:',3,'면적과둘레:',result)
    res1,res2=circle_area_circumference(3,3.14)
    print('반지름:',3,'면적:',res1,'둘레:',res2)

print('-------------------------------')

def circle_area1(radius,pi=3.14):
    area=pi*(radius**2)
    return area

if __name__=="__main__":
    print('반지름:',3,'면적:',circle_area1(3,3.14))
    print('반지름:',3,'면적:',circle_area1(3))

print('-------------------------------')

def circle_area2(radius,pi):
    area=pi*(radius**2)

if __name__=="__main__":
    print('반지름:',3,'면적:',circle_area2(3,pi=3.14))
    print('반지름:',3,'면적:',circle_area2(radius=3,pi=3.14))
    print('반지름:',3,'면적:',circle_area2(pi=3.14,radius=3))
    #print('반지름:',3,'면적:',circle_area2(radius=3,3.14))

print('-----------------------------------------------')

def do_any_sum(*num):
    sum=0
    for su in num:
        sum+=su
    return sum

if __name__=="__main__":
    print('합계:',do_any_sum(1))
    print('합계:',do_any_sum(1,2,3))
    print('합계:',do_any_sum(1,4,5,7,8))
    print('합계:',do_any_sum())

print('-----------------------------------------------')

def circle_area(radius,*pi,**info):
    for item in pi:
        area=item*(radius**2)
        print('반지름:',radius,'PI:',item,'면적:',area)

    for key in info:
        print(key,':',info[key])

if __name__=='__main__':
    circle_area(3,3.14,3.1456,3.141592)
    print()
    circle_area(3,3.14,3.1456,line_color='red',area_color='green')

print('-----------------------------------------------')
