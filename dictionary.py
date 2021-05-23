#딕셔너리 : 단어, 뜻이 있는 사전처럼 키와 밸류형태
#키값은 스트링도 가능
cabinet = {3:"유재석", 100:"조세호"}

#값 가져오는 법1
print(cabinet[3]) #[]안에 있는 값 : 키값
print(cabinet[100])
#값 가져오는 법2
print(cabinet.get(3)) 

#[]와 get 차이
#[]는 cabinet에 5라는 키가 없어 에러가 발생 -> 프로그램 종료
#get은 None이라고 출력을 하고 계속 이어갈 수 있다
#print(cabinet[5])
#None이라는 글자말고 기본값을 사용하고싶은 경우
print(cabinet.get(5,"사용가능"))
print("hi")

#값이 있는지 확인
print( 3 in cabinet) #True
print( 5 in cabinet) #False

#새값 할당
cabinet["5"] = "조세호"
print(cabinet)
#기존 값이 있는 경우, 덮어쓰기됨
cabinet["5"] = "김종국"
print(cabinet)

#원하는 키 값 삭제
del cabinet["5"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#전체 삭제
print(cabinet.clear())
print(cabinet)