import os
first = open("C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6/2/demo.txt", "r")
second = open("C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6/2/second7.txt", "a")
for lines in first:
    second.write(lines)


