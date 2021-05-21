#방법 1
print("나는 %d살입니다" % 20)

print("나는 %s을 좋아해요" % "파이썬")

#한글자만 받겠다 %c = char
print("Apple은 %c로 시작해요" % "A" )

print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

#format()안 값을 {}에 삽입
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간"))
#format뒤에 있는 파라미터를 0과 1인식
print("나는 {0}색과 {1}색을 좋아해요" .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age=20))

#파이썬 3.6이상
age = 20
color = "빨간"
#문장앞에 f를 선언하면, 변수에 저장된 값을 사용할 수 있다
print(f"나는 {age}살이며, {color}색을 좋아해요")