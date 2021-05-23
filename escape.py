print("백문이 불여일견 \n 백견이 불여일타")

print("저는 \n \"누구\"입니다.")
print('저는 "누구"입니다.')

print("문장 슬래쉬 \\")

# \r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("tab\ttab")


# 퀴즈 : 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
# 예 ) http://naver.com
# 규칙 1  : http://naver.com => naver.com
# 규칙 2 : 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 예 ) 생성된 비밀번호 : nav51!
site = "https://naver.com";

site = site[8:-4];

len2 = len(site);
print(site+str(len))

password = site[0:3]+str(len2)+str(site.count('e'))+'!'
print(password)

url = "http://naver.com";
my_str = url.replace("http://", ''); #규칙1
my_str = my_str[:my_str.index(".")] #규칙2 0부터 5직전까지

password2 = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다.".format(url, password2))



