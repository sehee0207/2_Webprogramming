import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0 
# 윈도 창의 폭, 높이, 펜 두께, 창 밖으로 빠져나간 횟수
r, g, b, angle, dist, curX, curY = [0] * 7
# 이동할 거리, 각도, 현재 거북이의 위치를 지정하는 변수

## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기') # 창 제목
turtle.shape('turtle') # 거북이 모양
turtle.pensize(pSize) # 펜 두께
turtle.setup(width=swidth+30, height=sheight+30) # 윈도 창 크기
turtle.screensize(swidth, sheight) # 안쪽 화면 크기 지정

while True : # while 문장으로 무한 반복
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    # 임의의 색상 설정
    
    angle =  random.randrange(0,360) # 각도는 0 ~ 360 범위
    dist = random.randrange(1,100) # 거리는 1 ~ 100 범위
    #각도 설정 후 거리만큼
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()
    # 현재 위치 구함

    # if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight):
    #     pass
    #     # 거북이의 현재 위치가 화면 안인지 체크
    #     # 중앙이 (0, 0)
    # else : # pass 실행해서 if 문을 그냥 종료하고 다시 while 수행, 범위를 벗어나면 else 실행
    #     turtle.penup() # 펜 사용 X
    #     turtle.goto( 0, 0 ) # 화면 중앙 이동
    #     turtle.pendown() # 다시 펜 사용
        
    #     exitCount += 1 # 거북이가 바깥으로 나간 횟수를 하나 증가
    #     if exitCount >= 5 : # 5회 이상 밖으로 나갔다면 break 문으로 while 빠져나간 후 프로그램 종료
    #         break

    if(-swidth / 2 <= curX and swidth / 2 >= curX) and (-sheight / 2 <= curY and sheight / 2 >= curY): pass
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        
        if exitCount >= 5: break

turtle.done()