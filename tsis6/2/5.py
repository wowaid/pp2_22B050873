import os
a = [i for i in input().split()]
f = open("C:\python2\week6\lab6\dirandfiles\demofor5.txt", "w")
for elem in a:
    f.write(elem + " ")
f.close()