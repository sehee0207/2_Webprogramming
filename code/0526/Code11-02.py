inFp = None
inStr = ""

inFp = open("D:/20402 김세희/s/0526/hello.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end = "")


inFp.close()
