#제어문: 코드의 흐름을 위부터 아래로 흐르지 않게 제어하는 것
#if문: 컴퓨터에게 선택의 여지와 조건 부여 = 분기문
#if(조건): 다음줄 indent
    #참이면 코드 실행

#예제 1
#85점 이상 PASS, 아니면 FAIL

score = int(input("점수를 입력하시오 : "))

if(score>=85):
    print("PASS")
else:
    print("FAIL")

#예제 2

activity = input("너 동아리 뭐해? ")
if(activity=="멋쟁이사자처럼"):
    print("어, 나도 멋사야!")
else:
    print("...okay")

#예제 3
#5000이상: 아웃백 / 3000이상: 학식 / 1000이상: 컵라면 / ㅠㅠ: 공기밥

money = int(input("너 돈 얼마 있어? "))

if(money>=5000):
    print("아웃백 가자")
else:
    if(money>=3000):
        print("학식 먹자")
    else:
        if (money>=1000):
            print("컵라면 먹자")
        else:
            print("공기밥 먹자")

#else if = elif

if(money>=5000):
    print("아웃백 가자")
elif(money>=3000):
    print("학식 먹자")
elif (money>=1000):
    print("컵라면 먹자")
else:
    print("공기밥 가즈아ㅏㅏ")