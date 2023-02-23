x=int(input())
def f(x):
    i=0
    while i<x:
        if i%12:
            yield i
        i+=1
for i in f(x):
    print(i)