# #문자열을 입력받아 반대로 출력

# ## 변수 선언 부분 ##
# inStr, outStr = "", ""
# count, i = 0, 0

# ## 메인 코드 부분 ##
# inStr = input("문자열을 입력하세요 : ")
# count = len(inStr)

# for i in range(0, count) :
#      ###### 코드 작성 부분
#     outStr += inStr[count-i-1]
#     i = i + 1
    

# print("내용을 거꾸로 출력 --> %s" % outStr)

inStr, outStr = "", ""
count, i = 0, 0

inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0, count) :
    outStr += inStr[count - i - 1]
    i += 1

print("내용을 거꾸로 출력 : %s" %outStr)