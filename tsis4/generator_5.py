x=int(input())

def f(x):
    while x>0:
        yield x
        x-=1
for i in f(x):
    print(i) 