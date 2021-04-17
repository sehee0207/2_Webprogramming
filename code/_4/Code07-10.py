## 변수 선언 부분 ##
colors = {"빨간색":"분홍색", 
            "하늘색":"베이지",
            "노란색":"하늘색",
            "민트색":"빨간색",
            "하얀색":"남색",
            "검은색":"하얀색",
            "그레이":"와인색" }

## 메인 코드 부분 ##
while (True) :
    mycolor = input(str(list(colors.keys())) + " 중 좋아하는 색은?")
    if mycolor in colors :
        print("<%s> 궁합 색은 <%s>입니다." % (mycolor, colors.get(mycolor)))
    elif mycolor == "끝" :
        break
    else :
        print("그런 색이 없습니다. 확인해 보세요.")
