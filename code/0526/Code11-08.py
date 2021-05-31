inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/win.init", "r")
outFp = open("D:\20402 김세희\0526\hello.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)


inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사 되었음")
