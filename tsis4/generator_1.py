x=int(input())
def f(x):
    i=1
    while i*i<x:
        yield i*i
        i+=1
for i in f(x):
    print(i)
    
