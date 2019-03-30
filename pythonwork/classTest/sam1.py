import ex.sam
ex.sam.aa()

s=ex.sam.Car()
s.show_info()

#aa 만 쓰겟다
from ex.sam import aa
aa()

#sam 파이썬 파일에서 aa 와 Car라는 함수 혹은 클래스를 받아서 사용하겟다
from ex.sam import aa,Car
aa()
s=Car()
s.show_info()

#sam 이라는 파이썬 파일에서 aa 라는 클래스 혹은 함수를 가져와서 a 로 명명하겟다
from ex.sam import aa as a
a()