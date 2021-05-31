ss = input("입력 문자열==> ")
print("출력 문자열==> ", end="")

if ss.endswith('(') == False :
    print("(", end = "")

print(ss, end="")

if ss.startswith(')') == False:
    print(")", end = "")

## ----------------------------------------- ##

inStr = "   한글Python 프로그래밍"
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ' :
        outStr += inStr[i]

print("원래 문자열==> " + '[' + inStr + ']')
print("공백 삭제 문자열==> " + '[' + outStr + ']')