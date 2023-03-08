import os
if os.path.exists("C:\python2\week6\lab6\dirandfiles\myfile.txt"):
  os.remove("C:\python2\week6\w3school\myfile.txt")
else:
  print("File does not exist!")