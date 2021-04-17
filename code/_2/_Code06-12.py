# i, hap = 0, 0
# for i in range(1, 11, 1):
#     hap = hap + i

# print("1에서 10까지의 합계 : %d" %hap)


# i, hap = 0, 0
# a1, a2 = 0, 0
# a1 = int(input("첫 번째 값을 입력하세요"))
# a2 = int(input("두 번째 값을 입력하세요"))


# if(a1 < a2):
#     for i in range(a1, a2+1, 1):
#         hap = hap + i
#     print("%d에서 %d까지의 합계 : %d" %a1 %a2 %hap)

# else:
#     for i in range(a2, a1+1, 1):
#         hap = hap + i
#     print("%d에서 %d까지의 합계 : %d" %a2 %a1 %hap)


hap = 0
a, b = 0, 0

while True:
    a = int(input("더할 첫 번째 수를 입력하세요"))
    b = int(input("더할 두 번째 수를 입력하세요"))

    if a == 0 or b == 0:
        break
    
    hap = a + b
    print("%d + %d = %d" %(a, b, hap))

print("0을 입력해 반복문에서 빠져나왔습니다")