inFp = None
inStr = ""
line = 1

inFp = open("./romeo story.txt")

inList = inFp.readlines()
for inStr in inList:
    print(line, end = "")
    line += 1
    print("| " + inStr, end="")

inFp.close()
