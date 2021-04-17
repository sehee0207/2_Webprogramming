aa = [0, 0, 0, 0]
hap = 0

for i in range(0, 4):
    aa[i] = int(input(str(i+1)+"번쨰 숫자"))
    hap = hap + aa[i]


print("합계 ==> %d" %hap)