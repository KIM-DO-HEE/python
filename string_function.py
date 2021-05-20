python = "Python is Amazing"
#문자열 소문자로
print(python.lower())
#문자열 대문자로
print(python.upper())
#대문자인지 소문자인지
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
#몇번째에 있는지
print(index)
#두번째 n을 찾게 된다
index = python.index("n", index + 1)

print(python.find("n"))
#원하는 값이 없을 경우 -1 반환
#index 함수 사용할 경우 에러 발생
print(python.find("java"));

#n이 몇번 등장하는지
print(python.count("n"))
