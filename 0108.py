"""
Lambda는 파이썬에서 익명 함수를 만들기 위한 키워드
일반 함수처럼 "def"를 사용하지 않고도 간단한 함수를 짧고 간결하게 정의 할 수 있디.
Lambda 함수는 1줄로 표현하는 함수이다.

기본 문법:
함수 이름 = Lambda 매개변수 : 표현식

lambda x, y: <-- 매개변수
x + y : <-- 표현식 혹은 리턴 명령어
"""
#기본 함수를 사용할 때
#def add(x, y):
#    return x + y
#value = add(3, 5)
#print (value)

#lamda를 사용할때
# add_lamda = lambda x, y: x + y
# print (add_lamda(3, 5))

# result = lambda x: x * 2 # 매개 변수가 1개 일때
# print(result(2))

"""
lamda와 함께 쓰이는 기능
map() 함수 #for문의 역할을 대신 할 수 있다.
map()은 리스트의 각 요소를 반환할때 사용
"""
# numbers = [1, 2, 3, 4, 5]
# new_number = []
# test = list(map(lambda x: x*2, numbers)) #map(함수, 리스트)
# #map함수를 사용 했을때에는 반환되는 값이 map object이기 때문에
# #다시 리스트로 값을 받기 위해 list()로 감싸줘야한다.
# print(test)

# str_list = ["1", "2", "3", "4", "5"]
# result = []

# for text in str_list:
#     result.append(int(text) + 1)
# print(result)

# # map함수를 사용할 때
# str_list = list(map(lambda x: int(x)+1, str_list))
# print(str_list)

# first_list = [1, 2, 3]
# last_list = [4, 5, 6]
# result = []

# for i, num in enumerate(first_list):
#     result = num + last_list[i]
#     print(result)

# for i in range(len(first_list)):
#     result = first_list[i] + last_list[i]
#     print(result)

# lambda_result = list(map(lambda x, y: x+y, first_list, last_list))
# print(lambda_result)

"""
lamda와 함께 쓰이는 기능
filter() 함수
filter()는 조건에 맞는 요소만 반환
"""
# numbers = [1, 2, 3, 4, 5, 6, 7]
# result = []
# for number, numbers in enumerate(numbers):
#     if number % 2 == 1:
#         result.append(numbers)
# print(result)

# new_list = []
# for number in numbers:
#     if number % 2 == 0:
#         new_list.append(number)
# print(new_list)

# #lamda 계산식
# even_num = list(filter(lambda x: x % 2 == 0, numbers))
# print (even_num)

# triangle_list = [7]
# triangle_list2 = [5]
# result = []

# triangle_area = lambda base, height : (base * height)/2
# print(triangle_area(7, 5))

# strings = ["hello", "world", "army_hotpot_oil_pasta"]
# string_words = list(map(lambda x, : x.upper(), strings))
# print(string_words)

# 모듈 사용하는 방법으로 계산 처리 스크립트 만들기
import shinyoung_module
# value_minus = shinyoung_module.minus(10, 3)
# value_add = shinyoung_module.add(10, 3)
# value_gopa = shinyoung_module.gopa(10, 3)
# value_nanu = shinyoung_module.nanu(10, 3)
# print (value_minus)
# print (value_add)
# print (value_gopa)
# print (value_nanu)

check_menu = shinyoung_module.menu_check
print (check_menu)

