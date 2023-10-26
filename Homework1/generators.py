def generator():
    num = 1
    while True:
        meows = ""
        for i in range(0,num):
            meows += "meow "
        num*=2
        yield(meows)

x= generator()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
