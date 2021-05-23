#리스트  : 순서를 따지는 객체 집합
#아래와 같은 여러개의 값을 하나로 연속적인 집합을 만드는 것
subway1 = 10
subway2 = 20
subway3 = 30 

subway = [10,20,30]

print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고있는지
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#뒤집기 
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5,1,4,2,3]
mix_list = ["조세호",20,True]
print(mix_list)

#여러개의 리스트를 하나의 리스트로 합칠 수 있다
num_list.extend(mix_list);
print(num_list)