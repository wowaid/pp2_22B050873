import os
first = open("C:\python2\week6\lab6\dirandfiles\demo.txt", "r")
second = open("C:\python2\week6\lab6\dirandfiles\secondd7.txt", "a")
for lines in first:
    second.write(lines)


