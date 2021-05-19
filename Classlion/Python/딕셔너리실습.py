#딕셔너리 실습 (내장함수)

pairs = {'잔나비' : '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소히':'산책', '홍크':'어쩌면'} #{'key':'value'}

#하나의 key-value 쌍을 추가하는 방법
#딕셔너리형 변수[새로운 키] = value

print(pairs)

pairs['스탠딩 에그'] = '휴식'

print(pairs)

#특정 key-value 쌍 삭제하는 방법: del 함수
# del 변수[key]

del pairs['잔나비']
print(pairs)

#key로 value 얻기: 변수.get(key)
pairs.get('소히') #너무 길면 다른 변수에 담아, value = pairs.get('소히') print(value) 이런식으로!
print(pairs.get('소히'))
