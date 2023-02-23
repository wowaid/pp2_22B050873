x=int(input())
def f(x):
    i=0
    while i<x:
        yield i
        i+=2
for i in f(x):
    print(i)