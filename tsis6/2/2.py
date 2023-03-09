import os

x = 'C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6/2/demo.txt'

def access(x):
    list = []

    if os.access(x, os.F_OK):
        list.append("file exists")
    else:
        list.append("file don't exists")

    if os.access(x, os.R_OK):
        list.append("file readable")
    else:
        list.append("file isn't readable")

    if os.access(x, os.W_OK):
        list.append("file writable")
    else:
        list.append("file isn't writable")

    if os.access(x, os.X_OK):
        list.append("file executable")
    else:
        list.append("file isnt't executable")
    return list
    
print(access(x))
print(access('C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6/2/demo1.txt'))