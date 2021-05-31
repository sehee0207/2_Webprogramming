inFp = None
inStr = ""

inFp = open("D:/20402 김세희/s/0526/hello.txt", "r") #파일 열기

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
