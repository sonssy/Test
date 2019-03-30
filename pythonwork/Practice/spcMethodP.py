#집합연산 메소드

class StudentScores(object):
    def __init__(self,data):
        self._data=data
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self,d):
        if d in self._data:
            return True
        else:
            return False

if __name__=='__main__':
    student_scores=StudentScores([90,95,100])
    print(len(student_scores))
    print(90 in student_scores)
    print(80 in student_scores)

a=[1,2,3,4]
print(1 in a)
a=[1,2,3,4]
print(5 in a)

print('---비교연산 메소드 예제--------------')

class Sam(object):
    def __init__(self,num):
        self._num=num
    def __eq__(self,other):                     # 여기를 주석처리하면 값이 바뀜
        return self._num == other._num
    def __bool__(self):
        return self._num>5

s1=Sam(7)
s2=Sam(3)
s3=Sam(7)
print(s1 == s3)            #윗부분을 주석처리(빼버리면)하면 값은 false
if s2:             #s1과 s3는 같지않기떄문에 주석처리안하면 안의 값이 7로 같음으로true
    print('크다')      
else:
    print('작다')