from __future__ import print_function
import os

path = '..'
dirpath = os.getcwd()

print("TEST: BEGIN\n")
print("TEST: current directory is : " + dirpath)
print("TEST: contents of .. is : ")

files = os.listdir(path)
for name in files:
    print(name)

print("TEST: END\n")
