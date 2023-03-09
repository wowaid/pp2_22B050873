import os
a = [i for i in input().split()]
f = open("C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6/2/demofor5.txt", "w")
for elem in a:
    f.write(elem + " ")
f.close()