import os
print("Test a path exists or not:")
path = r'demoo.txt'
print(os.path.exists(path))
path = r'C:\python2\week6\w3school\writecreatefiles.py'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))