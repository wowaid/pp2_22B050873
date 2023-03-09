import os
print("Test a path exists or not:")
path = r'demo.txt'
print(os.path.exists(path))
path = r'C:/Users/damir/OneDrive/Рабочий стол/papkaa/pp2/pp2_22B050873/tsis6'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))