a=int(input())
b=int(input())
def f(a,b):
    while a<b:
        yield a*a
        a+=1
        if a*a==b:
            break
for i in f(a,b):
    print(i)