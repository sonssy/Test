class A:
    def func1(self):
        print('super')
class subA1:
    def func1(self):
        print('subA1')
class subA2:
    def func1(self):
        print('subA2')

def printA(a):
    a.func1()

a=A()
a1=subA1()
a2=subA2()
print('-----')
a.func1()
a1.func1()
a2.func1()
print(a)
print(a1)
print(a2)

print('=======================================================')

class B:
    def pr(self):
        print("B")

class SubB1(B):
    def pr(self):
        print("pr1")

class SubB2(B):
    #def pr(self):
    #    print("pr1")
    pass

s=SubB1()
s1=SubB2()
s.pr()
s1.pr()
print('----------------------')