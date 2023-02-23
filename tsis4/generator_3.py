x=int(input())
def f(x):
    i=0
    while i<x:
        yield i
        i+=12
for i in f(x):
    print(i)