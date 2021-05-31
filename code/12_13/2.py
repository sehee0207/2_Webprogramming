inStr, outStr = "", ""
inStr = input('문자열 --> ')
for i in range(0, len(inStr)) :
    if(inStr[i] != '0' and inStr[i] != '1' and inStr[i] != '2' and inStr[i] != '3' and inStr[i] != '4' and inStr[i] != '5' and inStr[i] != '6' and inStr[i] != '7' and inStr[i] != '8' and inStr[i] != '9'):
        outStr += inStr[i]

print('숫자 제거 --> ' + outStr)