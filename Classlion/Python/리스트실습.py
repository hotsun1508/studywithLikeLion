#리스트 실습 (내장함수)

li = [3, 1, '움칫', 4, "둠칫", 5, 1]

#인덱싱 슬라이싱
print(li[1:3])

#리스트의 길이를 구해주는 함수: len(변수)
print(len(li))

#리스트 원소 오름차순 정렬해주는 함수: 변수.sort()
#sort는 list자체를 반환하는 함수가 아님, print(li.sort()) -> 이렇게 쓰기 불가능
print(li)
sorted = li.sort() #배열에 숫자가 있으면 안됨
print(sorted) #print(li)이렇게 변수에 담아도 됨

#리스트 내 특정 원소 인덱스 반환해주는 함수 : 변수.index(요소)
print(li.index("움칫"))

#리스트 내 특정원소 갯수 세기: .count(요소) 
print(li.count(2))
