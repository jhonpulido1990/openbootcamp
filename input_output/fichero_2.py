#!/usr/bin/python3

myfile = open("texto.txt", "r")
myline = myfile.readline()
while myline:
    print(myline)
    myline = myfile.readline()
myfile.close()
