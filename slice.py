jumin = "990120-1234567"

#필요한만큼 잘라서 사용 -> slice
print("성별 : " + jumin[7])

print("연 : "+ jumin[0:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 : "+ jumin[:6]) # 처음부터 6직전까지

print("뒤 7자리 :" + jumin[7:]) # 7부터 마지막까지
print("뒤 7자리 (뒤에부터) :" + jumin[-7:]) #맨 뒤에서 7번째 끝까지


