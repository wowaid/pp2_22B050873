import os

path = 'C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6'

os.mkdir(f'{path}/alphabet')

os.chdir(f'{path}/alphabet')


for i in range (65, 91):
    open(chr(i) + '.txt', 'x')