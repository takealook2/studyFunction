#제어문 실습
#분기문
# if(조건):
#   실행문

#예제1) 85점 이상이면 pass, 85점 이하이면 fail 출력해 보자!
# score = int(input("점수를 입력하세요: "))
# if(score>=85):
#     print("pass")
# else:
#     print("fail")

#예제2) 친구한테 멋사자인지 물어보고, 멋사자이면 기쁨의 반응을 아니면 시무룩한 반응
# activity = input("너 동아리 멋쟁이 사자처럼이야?")
# if(activity=="응"):
#     print("어! 나도 멋사자야!")
# else:
#     print("아..그래...")

#예제3) 친구와 밥을 먹을 건데, 친구 수중에 있는 돈에 따라서 메뉴를 골라보자
#오만원 이상이면 아웃백, 만원 이상이면 학식
#오천원 이상이면 컵밥, 천원 이상이면 컵라면
#천원 미만이면 집에 가서 먹자
money = int(input("너 돈 얼마있어?"))
if(money>=50000):
    print("아웃백을 가자!")
elif(money>=10000):
    print("학식 먹으러 가자!")
elif(money>=5000):
    print("컵밥 먹으러 가자!")
elif(money>=1000):
    print("컵라면 먹으러 가자!")
else:
    print("집이나 가자")

#반복문예
#ex) num에 1씩 더하다가 3을 만났을 때 반복문을 정지시켜보자.
# num = 0
# while(True):
#     print(num)
#     num += 1 #num = num + 1
#     if(num== 3):
#         break

#ex2) 1~10의 범위 중 홀수만 출력해보자
# for i in range(10):
#     if(i%2==0):#짝수
#         continue
#     print(i)