inFp = None
inList, inStr = [], ""
line = 1;

inFp = open("D:/20402 김세희/s/0526/hello.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    print(line, end = "")
    line += 1
    print(" : " + inStr, end="")


inFp.close()
