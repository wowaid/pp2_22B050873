def has__33(ls):
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1] == 3:
            return True
    return False


l = list()
print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
for i in range(n):
    x = int(input())
    l.append(x)
print(has__33(l))