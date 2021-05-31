inFp, outFp = None, None
inStr, outStr = "", ""
first = input("입력 파일명을 입력하세요 : ")
end = input("출력 파일명을 입력하세요 : ")

with open(first, 'r', encoding = 'utf-8') as inFp:
    inStr = read(inFp)
    with open(end, 'w', encoding = 'utf-8') as outFp:
        outStr += inStr
        outFp.write(outStr)
        
print(' %s --> %s 변환 완료' % (first, end))
