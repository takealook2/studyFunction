#리스트 실습
# li = [3, 1, "배가", 4, "고파요", 5, 1]

#리스트 인덱싱
# print(li[2])

#리스트 슬라이싱
# print(li[0:4])

#1_리스트 길이를 구해주는 내장함수 : len(리스트 변수명)
# print(len(li))

#2_리스트를 오름차순으로 정렬해 주는 내장함수 : 리스트변수명.sort()
# li2=[3, 1, 4, 5, 2]
# li2.sort()
# print(li2) #sort는 원본 리스트를 정렬시켜준다.

#참고 : sorted 원본 배열함수를 건들지 않고 sorted를 사용하는 순간 새로운 함수를 만든다.
# li3=sorted(li2)
# print(li3)

# print(li2)
# li2.sort()
# print(li2)

# sort()로 내림차순 하는 법을 구글링해서 알아보도록 하자! (보너스 과제)
# 여기에 코드를 적어주세요(print문 사용)
li = [1,5,2,4,8]
li.sort(reverse=True)
print(li)

#3_리스트 내의 특정 원소 인덱스를 반환하는 함수 : 리스트변수.index()
# print(li.index("배가"))

#4_리스트 내의 특정 원소의 개수를 세어주는 함수 : 리스트변수.count(요소)
# print(li.count(1))

