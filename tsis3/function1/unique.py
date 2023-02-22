def unique_array(l):
    ans =[]
    for i in l:
        if i not in ans:
            ans.append(i)
    return ans        

print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list(map(int, input().split()))
print(unique_array(l))