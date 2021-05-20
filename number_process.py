#숫자처리함수
print(abs(-5))

print(pow(4, 2)) # 4 ^ 2 = 16
print(max(5,12)) # 12
print(min(5,10)) # 5
print(round(3.14)) # 3
print(round(4,99)) # 5

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림 4
print(sqrt(16)) #제곱근 결과값 : 4

#랜덤함수
from random import *

print(random()) # 0.0이상 1.0미만의 임의의 값 생성
print(random () * 10) #0.0 ~ 10.0미만의 임의의 값 생성
print(int(random() * 10)) #0부터 10미만의 임의의 값
print(int(random() * 10) +1) # 1부터 10 이하의 임의의 값 출력

print(int(random() * 45) + 1) # 1 ~45이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~45이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~45이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~45이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~45이하의 임의의 값 생성
print(int(random() * 45) + 1) 

# 1 ~45이하의 임의의 값 생성

#위의 코드를 한줄로 요약할 수 있음
print(randrange(1,45)) #1~45미만의 임의의 값 생성
print(randrange(1,46)) #1~45이하의 임의의 값 생성

print(randint(1,45)); # 1~45이하의 임의의 값 생성

#퀴즈 : 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 
#하기로 했습니다. 아래 조건에 맞는 오프라인 모임날짜를 정해주는
#프로그램을 작성하시오

#조건 1 : 랜덤으로 날짜를 뽑아야함
#조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
#조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

#출력문 예제
#오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다
day = randint(4,28);

print("오프라인 스터디 모임 날짜는 매월 "+str(day)+"일로 선정되었습니다")