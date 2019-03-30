import time as t

print(t.time())

def call_by_val(num,mlist):
    num = num+1
    mlist.append("add1")

num=10
mlist=[1,2,3]

print(num,mlist)
call_by_val(num,mlist)
print(num,mlist)

def hello_message():
    print("Hello")

if __name__=="__main__":
    hello_message()