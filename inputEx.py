name = input('이름을 입력하세요')
age = input('나이를 입력하세요')

print(name + age)

print('제 이름은', name , '입니다. 제 나이는', age, '입니다')
print('제 이름은 {} 입니다. 제 나이는 {} 입니다.'.format(name, age))
print('제 이름은 %s 입니다. 제 나이는 %s 입니다.' % (name, age))
