#문자열을 입력받아 그중 o를 $로 변경하는 문자열 변경을 응용


# ss = input("입력 문자열 ==> ")

# print("출력 문자열 ==> ", end = '')
# for i in range(0, len(ss)) :
#      if(ss[i] != 'o') : ##코드 작성 부분
#           print(ss[i], end = '')
#      else :
#           print('$', end = '')

ss = input("입력 문자열 ==> ")

print("출력 문자열 ==> ", end="")
for i in range(0, len(ss)) :
     if(ss[i] == 'o') :
          print('$', end="")
     else :
          print(ss[i], end="")