# 입력한 숫자의 각 자리수 별찍기

i, k = 0, 0
a = 0
a1, a10, a100 = 0, 0, 0

while True:
    a = int(input("1이상, 999이하의 나타낼 숫자를 입력하세요"))

    if(a>=1000):
        print("숫자를 다시 입력하세요.")
    
    else:
        break

a100 = int(a / 100)
a10 = int(a/10 - a100*10)
a1 = int(a % 10)
print("")

print("%d" %a100, end=' ')
for i in range(0, a100, 1):
    print("*", end='')
print("")

print("%d" %a10, end=' ')
for i in range(0, a10, 1):
    print("*", end='')
print("")

print("%d" %a1, end=' ')
for i in range(0, a1, 1):
    print("*", end='')
print("")