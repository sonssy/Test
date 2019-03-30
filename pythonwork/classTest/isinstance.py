print(type(1))
print(isinstance(1,int))
print(isinstance(1.0,int))
print(type('kor'))
print(isinstance('kor',str))
class Sam1:
    pass
s1=Sam1()
print('s1',isinstance(s1,Sam1))
print(isinstance('kor',object))
print(isinstance({},dict))