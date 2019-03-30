def hello_message(repeat_count):
    for item in range(repeat_count):
        print('HELLO WORLD')

if __name__=="__main__":
    a=hello_message(1)
    hello_message(2)
    print(a)