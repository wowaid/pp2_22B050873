str = input()
cnt1, cnt2 = 0, 0
for letter in str:
    if letter.islower():
        cnt1 += 1
    elif letter.isupper():
        cnt2 += 1
print("Number of uppercase letters:" , cnt2)
print("Number of lowercase letters" , cnt1)