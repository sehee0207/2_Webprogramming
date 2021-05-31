# #문자열 중간의 공백까지 삭제해 주는 코드


# inStr = "   한글 Python 프로그래밍   "
# outStr = ""

# for i in range(0, len(inStr)) :
#      if (inStr[i] != ' '):
#           outStr += inStr[i]
#           ##코드 작성 부분
          

# print("원래 문자열 ==> " + '[' + inStr + ']')
# print("공백 삭제 문자열 ==> " + '[' + outStr + ']')

inStr = "      python     programming"
outStr = ""

for i in range(0, len(inStr)) :
     if(inStr[i] != ' ') :
          outStr += inStr[i]

print("원래 문자열 ==> " + '[' + inStr + ']')
print("공백 제거 문자열 ==> " + '[' + outStr + ']')