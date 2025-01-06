# money = True #Boolean 자료형
# if money:
#     print ("세금을 내세요")
# else:
#     print("안내도 괜찮아요")

# salary = 4000
# if salary > 5000:
#     print("세금을 내세요")
# else:
#     print("세금을 안내도 괜찮아요")

# a = [1, 2, 3]
# if 1 in a:
#     print("있습니다")
# else:
#     print("없습니다")

# baguni = ["a", "b", "c"]
# for abc in baguni:
#     if abc == "a":
#         print("a 입니다")
#     elif abc == "b":
#         print("b 입니다")
#     else:
#         print("c 입니다")

# import random
# number = random.randint(1, 10)

# for random_number in range(1, 6):
#     Myrandom_num = int(input("1~10중 숫자를 입력해주세요:) : "))
#     print(number)

#     if Myrandom_num not in range(1,11): # list를 반환하지 않는다.
#         print("잘못입력하셨습니다")
#         continue

#     if Myrandom_num == number:
#         print(f"정답입니다. {random_number}번 만에 맞추셨네요:)")
#         break  
#     elif Myrandom_num > number:
#         print("숫자가 높아요ㅜ")
#     elif Myrandom_num < number:
#         print("숫자가 낮아요ㅜ")        
#     elif Myrandom_num != number:
#         print("틀렸어요ㅠ")      

"""
기본적인 사칙연산
print (1+2) # 더하기
print (1-2) # 빼기
print (1*2) # 곱하기
print (1/2) # 나누기
print (1%2) # 나누어서 나머지를 반환
print (1//2) # 나누어서 몫을 반환
"""




"""
while 반복문
while문은 조건이 참(True)인 동안 반복적으로 코드를 실행하는 반복문
조건이 거짓(False)가 되면 반복이 종료됨
while문은 반복 횟수가 정해져 있지 않거나, 특정 조건을 만족할 때까지 반복이 필요할때 쓰인다.

기본문법:
while 조건:
    #실행될 코드
"""

# count = 0
# while count < 5:
#     print(f"Count : {count}")
#     count +=1

# 사용자가 입력하는 숫자가 1234가 맞을때까지 계속 입력을 요구하는 스크립트
# user_input = ""
# while user_input != "1234":
#     user_input = input("1234를 입력해주세요. : ")
# print("감사합니다.")

# 반복문 종료
# count = 0
# while True:
#     if count == 5:
#         break
#     if count == 3:
#         continue  #밑의 스크립트를 작성시키지 않고 넘기겠다.  
#     print(f"Count : {count}")
#     count +=1

 #숫자 더하기
# Total = 0

# while True:
#     My_input = input("숫자를 입력해주세요 : ")

#     if My_input == "exit":
#         print("종료됩니다.")
#         break 

#     Total += int(My_input)
#     print(f"Total : ({My_input} + {Total} = {Total})")

# + = 1
# - = 2
# * = 3

# Total = 0

# while True:
#     num1 = input("숫자를 입력해주세요 : ")
#     if num1 == "exit":
#         print("종료됩니다.")
#         break 
#     if num1 == "clear":
#          Total = 0
#          print(f"결과 값이 초기화 됩니다. {Total}")
#          continue

#     My_middle = input("계산식을 추가해주세요 : ")  
#     num2 = input("추가 할 숫자를 입력해주세요 : ")
    
#     if My_middle == "+":
#         Total = int(num1) + int(num2)
#         print(f"Total : {num1} + {num2} = {Total}")
       
#     elif My_middle == "-":
#         Total =  int(num1) - int(num2)
#         print(f"Total : {num1} - {num2} = {Total}") 

#     elif My_middle == "*":
#         Total = int(num1) * int(num2)
#         print(f"Total : {num1} * {num2} = {Total}")

#     elif My_middle == "/":
#         Total = int(num1) / int(num2)
#         print(f"Total : {num1} / {num2} = {Total}")

        
"""
Boolean 자료형이란?
참 또는 거짓을 나타내는 자료형으로, 논리 자료형이라고 한다.
Boolean 자료형은 줄여서 불(Bool) 자료형이라고도 한다.

특징
1. True, False를 사용할때에는 꼭 첫글자가 대문자여야한다.
2. False는 숫자1, False는 숫자 0으로 취급할수 있다.
3. 대부분의 객체는 Bool()로 평가할수 있으며, 값이 있을때 True로 간주한다
"""             

# a = True
# a = [1, 2, 3, 4]

# if a:
#     print("참 입니다.")
# else:
#     print("거짓입니다.") #a = []일때

"""
문자열 슬라이싱 2번째
Split() 명령어는 문자열의 특정 구분자를 기분으로 나누어 리스트로 반환하는 명령어
이는 문자열을 다룰 때 유용함

기본문법 :
text.split(separator=None)
separator : 문자열을 나눌 기준으로 기본 값은 공백으로 처리

"""
# text = "Hello, World"
# temp = text.split(",")

# print (temp)
# hello = temp[0]
# world = temp[1]

# # hello = text.split(", ")[0]
# # world = text.split(", ")[1]
# print (hello)
# print(world)

# text = "bom yeorum gaeul gyeoul"
# temp = text.split()
# print (temp)

# text = "bom, yeorum, gaeul, gyeoul"
# temp = text.split(",")
# print (temp)

# user_input = input("아무 숫자나 콤마로 구분하여 입력해주세요 : ")
# numbers = user_input.split(",")
# print (numbers)



# file_path = "/show/squidgame2/seq/shot/OPN_0010/comp/OPN_comp_v001.nk"
# split = file_path.split("/")
# project_name = split[2]
# shot_name = split[5]
# team = split[6]

# print(project_name, shot_name, team)


# text = "strawberry,melon,podoo"
# split = text.split(",")
# new_text = "-".join(split)
# new_text = f"{split[0]}-{split[1]}-{split[2]}" #join이 없을때 사용하는 방법
# print(text)
# print(split)
# print(new_text)

"""
Tuple은 기본 데이터 구조 중 하나로, 여러 값을 하나의 묶음으로 저장할 수 있는 불변 자료형
리스트와 비슷하지만 튜플은 생성 후 값을 변경할 수 없다.

특징
1. 요소의 값을 변경하거나 삭제할 수 없다.
2. 데이터를 안전하게 보관해야할때 사용한다.
3. 저장된 순서대로 값이 유지된다.
4. 중복이 허용된다.

* 데이터를 조회하는 속도가 리스트보다 빠르다.
* 메모리 사용량이 리스트보다 적다.
* 변경되지 않는 데이터의 경우 튜플을 사용한다.
"""

# # my_tuple = (1, 2, 3)
# my_tuple = 10, 20, 30
# print(my_tuple.index(20))

"""
딕셔너리 키(key) - 값(Value)가 쌍으로 데이터를 저장하는 가변 데이터 구조
중괄호 {}로 정의하며, 키를 통해 값에 접근 가능
"""
# my_dict = {"name": "shinyoung", "age": 23, "hobby": ["camping","python"]}
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["hobby"])

# my_dict = {}
# my_dict["name"] = "shinyoung"
# my_dict["age"] = 23
# my_dict["hobby"] = ["camping","python"]
# print(my_dict)

# print(my_dict.keys()) #딕셔너리가 현재 가진 모든 키를 리스트로 반환한다.
# print(my_dict.values()) #딕셔너리가 현재 가진 모든 값을 리스트로 반환한다.

# for key, value in my_dict.items():
#     if key == "name":
#         print (key, value)

# scores = {}
# scores["junsu"] = [100, 90, 80]
# scores["shinyoung"] = [30, 50, 10]
# scores["joohye"] = [80, 90, 90]

# for key, value in scores.items():
#     if key == "shinyoung":
#         total = sum(value)
#         count = len(value)
#         result = total / count
#         print(f"{key}님의 평균은 {result} 입니다.")


# data = [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit"), ("garlic", "vegetable"), ("podo", "fruit"), ("tomato", "vegetable")]

# my_dict = {} # 딕셔너리 선언

# for item_name, category in data:
#     print (item_name, category) 
#     if category in my_dict.keys():
#         my_dict[category].append(item_name) #에러가 나는 이유는 리스트가 없어서 
#     else:
#         my_dict[category] = []
#         my_dict[category].append(item_name)
# print(my_dict)

# gain_dict = {}
# name = input("이름을 입력해주세요 : ")
# age = int(input("나이를 입력해주세요 : "))
# major = input("전공를 입력해주세요 : ")

# gain_dict["name"] = name
# gain_dict["age"] = age
# gain_dict["major"] = major

# student_dict = {}
# student_dict["C275097"] = gain_dict
# print (student_dict)


"""
File i/o
파일 입력과 출력은 파일 입출력 기능을 통해 처리 할 수 있다.
이를 위해 파이썬은 내장함수인 open()을 제공한다.
이 명령을 이용해서 읽기, 쓰기, 추가 등의 작업을 진행 가능하다.
작업이 완료되면 반듯이 닫아야 한다.

파일 열기 모드
r 읽기 모드
w 쓰기 모드
a 추가 모드
"""

# with open("/home/rapa/My_Python/My_Python0102/text.txt", "r") as file:
    # content = file.read() # 파일 내용 읽기
    # print (content)
    # for line in file: #파일 내용을 한줄씩 읽는다.
    #     print (line)
    # lines = file.readlines() # 파일 내용을 한줄씩 리스트의 요소르 받는다.
    # print(lines)

#파일 쓰기 방법
# with open("/home/rapa/My_Python/My_Python0102/text.txt","w") as file:
#     file.write("안뇽하세루\n")
#     file.write("지금은 17:01분\n")
#     file.write("집가기 1시간 전\n")    

#파일 내용 추가
# with open("/home/rapa/My_Python/My_Python0102/text.txt","a") as file:
#     file.write("언제나 설레는 집 가는 길~\n")


# op_list = ["+", "-", "*", "/"]
# round_num = 2

# # 소개
# print("계산기")
# print()
# print("exit, clear 커맨드 입력이 가능합니다")


# total = 0.0
# while True:
#     print("계산 식을 입력해 주세요. (ex. 1 + 1, 혹은 - 2)")
#     user_input = input()

#     # 사용자 커맨드 입력 처리
#     if user_input == "exit":
#         break
#     elif user_input == "clear":
#         total = 0.0
#         print("초기화 되었습니다")
#         continue

#     # 사용자 입력을 숫자로 전환, 에러시 continue
#     try:
#         splited_input = user_input.split(" ")

#         # 2개의 입력 처리 (- 2와 같은 입력)
#         if len(splited_input) == 2:
#             num1 = total
#             op, num2 = splited_input

#         # 3개의 입력 처리 (1 + 1과 같은 입력)
#         elif len(splited_input) == 3:
#             num1, op, num2 = splited_input
#         else:
#             print("잘못된 식을 입력하셨습니다.")
#             continue

#         num1, num2 = float(num1), float(num2)
#     except ValueError:
#         print("잘못된 식을 입력하셨습니다.")
#         continue
    
#     # 연산자 검사
#     if op not in op_list:    
#         print("잘못된 연산자를 입력하셨습니다. (+, -, *, /) 안에 있는 연산자를 입력해 주세요")
#         continue
    
#     # 연산
#     if op == "+":
#         total = num1 + num2

#     elif op == "-":
#         total = num1 - num2

#     elif op == "*":
#         total = num1 * num2

#     elif op == "/":
#         # 0으로 나눌 수 없는 예외처리
#         if num2 == 0:
#             print("0으로 나눌 수 없습니다.")
#             continue
#         total = num1 / num2

#     print(round(total, round_num))
