# lam mot app nhac nho cong viec
# doc file txt chua cac cong viec can lam
# cu 5 ph nhac mot lan

import time
import sys
from itertools import islice




def readFile(file_location):
    search = open(file_location, "r")
    f = open("/home/do/PycharmProjects/result.txt", "a")

    for line in search:
        c = '1'
        p = len(line) - 3

        if "name" in line:
            line = line[:p] + c + '"' + ','
            f.write(line + "\n")
            print(line + "\n")
        else:
            print(line)
            f.write(line)
    #print(search.read())

def updateFile(file_location):
    #num = raw_input("name")
    #f = open(file_location, "a")
    search = open(file_location)
    for line in search:
      #if num in line:
        print(line)
    #f.write("Now the file has more content!\n")
    #f.close()
    #search.close()

readFile("/home/do/PycharmProjects/todo.txt")
#updateFile("/home/do/PycharmProjects/todo.txt")

