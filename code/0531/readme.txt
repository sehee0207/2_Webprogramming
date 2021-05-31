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

--------------------------------------------------------------------------------------

1) 입력 파일명을 inFp 라는 변수 이름으로 입력 받고
2) 파일 속 내용을 inStr 변수에 저장
3) 출력 파일명을 outFp 라는 변수 이름으로 입력 받은 뒤에
4) 비어있는 변수인 outStr 변수에 inStr 저장
5) outFp 파일에 outStr 변수에 있는 내용 즉 inStr 변수의 내용을 적어주고
6) with - as 문을 사용해서 자동으로 close 되도록 하였음