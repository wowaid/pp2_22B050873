def histogram(l):
    ll=[]
    for i in l:
        ll.append('*'*i)
    return ll 
print(*histogram(list(map(int, input().split()))), sep='\n')    
