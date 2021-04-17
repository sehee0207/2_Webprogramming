myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

#넣기
myList.append(40)
print("append(40) 후의 리스트 : %s" %myList)

#빼기
print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" %myList)

#정렬, 알파벳 + 작은 숫자부터
myList.sort() 
print("sort() 후의 리스트 : %s" %myList)

myList.reverse()
print("reverse() 후의 리스트 : %s" %myList)

print("20값의 위치 : %d " %myList.index(20))

#(몇 번쨰 인덱스, 어떤 값)
myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" %myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" %myList)

#그냥 뒤에 추가
myList.extend([77, 88, 77]) 
print("extend([77, 88, 77]) 후의 리스트 : %s" %myList)
print("77값의 개수 : %d" %myList.count(77))