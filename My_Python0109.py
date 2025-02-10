import random

# lambda 복습
# add_lamda = lambda x, y : x+y

# numbers = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x+1, numbers))
# print(new_list)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # 조건에 맞는 데이터를 반환할때는 filter 사용
# print(even_numbers)

# # 외부의 파일을 불러오기
# import sys 
# sys.path.append("/home/rapa/My_Python/My_Python0108")
# # 현재 시스템 패스에 커스텀 경로를 추가한다.

# import shinyoung_module
# # 추가된 경로에 있는 파이썬 모듈을 호출한다. 
# v = shinyoung_module.add(5, 3)
# print(v)


"""
리스트 컴프리핸션은 파이썬에서 리스트를 생성하는 간결하고 직관적인 방법
기존의 for루프롸 조건문을 한줄로 적어 코드가 짧고 읽기 쉬워진다.

기본 문법
[표현식 for 요소 in 반복가능한 객체(이터러블 데이터) if 조건]
"""
# numbers = [1, 2, 3, 4, 5]
# list(range(6)) # 2번 방법

# numbers = []
# for i in range(6):
#     numbers.append(i) # 3번 방법

# numbers = [ i*5 for i in range(6) ]
# print(numbers)

# even_numbers = [ x for x in range(1, 11) if x % 2 == 0 ]
# # if 조건문을 쓸때는 반복문 기준 오른쪽에 작성

# even_numbers = [x if x % 2 == 0 else "홀수" for x in range(1, 11) ]
# # if - else를 같이 쓸때는 반복문 기준 왼쪽에 작성
# print (even_numbers)

#기존의 사용 방식
# for i in range(2, 9):
#     for j in range(1, 9):
#         result = i * j
#         print (f"{i} x {j} = {result}")

# #리스트 컴프리헨션을 사용할 때
# gugudan = [ f"{i} x {j} = {i * j}" for i in range(2, 10) for j in range(1, 10) ]
# print(gugudan)

# # 리스트
# a = [ 1, 2, 3, [4, 5] ]
# # print (a[3][0])

# a = []
# b = [1, 2, 3]
# c = [4, 5]
# d = [6, 7, 8]
# a.append(b)
# a.append(c)
# a.append(d)

# result = []
# for i in a:
#     for j in i:
#         result.append(j)
# print(result) 

# # 1. 중첩되지 않는 리스트 만들기
# mixed_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat_list = [j for i in mixed_list for j in i]
# print(flat_list)

# #2. 문자열을 리스트 단어를 뒤집어서 리스트에 추가
# words = ["apple", "banana", "cherry"]
# reverse_words = [fruit[:: -1] for fruit in words]
# print (reverse_words)

# # 3. 주어진 리스트에서 양수 출력
# numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
# positive_number = [ i for i in numbers if i > 0 ]
# print(positive_number)

# # 4. 주어진 문자열의 알파벳만 문자열로 출력하기 ( str.isalpha())
# text = "I was born in 2000"
# abc = [i for i in text 
# if i.isalpha() == True]
# print(abc)

"""
정규 표현식
Regular Expression이란 복잡한 문자열을 처리하는 기법으로
모든 언어에서 공통적으로 사용하는 익스프레션
줄여서 정규식이라고 이야기 한다.
이 정규식은 찾으려는 문자열의 "패턴"을 설정해서
대상 문자열에서 패턴과 일치하는 문자를 객체로 반환하여 사용된다.
"""

# # 기존의 split를 사용하는 방법(관리에 취약)
# file_name = "OPN_0010_anim_v013.mb"
# temp = file_name.split("_")
# print(temp)
# version = temp[3].split(".")[0]
# print(version)

# #정규식을 사용하여 표현하기 (버전 가져오기)
import re # Regular Expression 모듈을 불러온다.
# file_name = "OPN_0015_anim_v022.mb" # 대상 문자열

# # p = re.compile("[v]\d{3}")
# # print(p)

# p = re.compile("[v]\d{5}")
# p_data = p.search(file_name)
# if p_data:                    # p_data 객체가 있을때
#     version = p_data.group()  # 객체 안의 데이터를 변수에 담겠다.

# p.search(file_name)
# data = p.search(file_name)
# version = data.group()
# print(version)

# re  모듈
# match - 문자열의 가장 처음이 패턴과 일치하면 객체를 리턴
# search - 문자열 중에 패턴과 첫번쨰로 매치되는 문자를 객채로 리턴
# findall - 문자열 중에 패턴과 매치되는 모든 문자를 리스트로 리턴
# finditer - 문자열 중에 패턴과 매치되는 모든 문자를 객체리스트로 리턴

# . : 줄바꿈을 제외한 모든 문자와 일치
# ^ : 문자열의 시작 부분에 대응
# $ : 문자열의 끝 부분에 대응
# + : 앞의 문자가 1회 이상 반복되는 부분에 매치
# ? : 앞의 문자가 0회 또는 1회 등장하는 부분에 매치
# {m , n} : 앞의 문자가 최소 1회, 최대 n회 반복되는 부분에 매치
# [] : 대괄호 안의 문자와 일치하면 매치
# () : 패턴을 그룹으로 묶어준다.
# | : OR 연산자


# text = "오늘은 2025년 1월 9일 입니다."
# p = re.compile("\d+")
# p_data = p.findall(text)
# print(p_data[0], p_data[1], p_data[2])

# # if p_data:
# #     today = p_data.group()
# # print(today)

# # p_data = p.search(file_name)
# # if p_data:                    # p_data 객체가 있을때
# #     version = p_data.group()

# text = "오늘은 2025-01-09 이고, 내일은 2025-01-10 입니다."
# p = re.compile("\d{4}-\d{2}-\d{2}")
# p_data = p.findall(text)
# print(p_data)


# phone_number = input("핸드폰 번호를 입력해주세요")
# my_number = "010-3333-3333"
# p = re.compile("\d{3}-\d{4}-\d{4}")
# p_data = p.match(phone_number)
# print(p_data)
# if p_data:
#     ver = p_data.group()
#     print(f"번호가 맞아요. {phone_number}")
# else:
#     print(f"{phone_number}는 잘못된 번호입니다.")
# # 010-3333-3333이 아닌 경우에는 다시 입력해달라 혹은 잘못된 번호다

"""
클래스란 객체 지향 프로그래밍에서 사용되는 개념으로, 
데이터와 해당 데이터를 처리하는 함수(메서드)를 하나로 묶어주는 개념
객체는 클래스의 인스턴스로 클래스에서 정의한 구조와 동작을 실제로 구현한 것
"""

# 기본 문법
# class ClassName:

#     def __init__(self): # 클래스가 생성될때 고정으로(지정돤 함수 이름)
#         """
#         생성자란 객체를 생성할 때 자동으로 호출되는 메서드로
#         주로 객체의 초기화 작업을 수행
#         """
#         print("생성자 입니다.")
#         self.junsoo_oppa()

#     # 인스턴스 메서드(함수) self를 첫번째 매개변수로 입력받아 인스턴스를 관리
#     def junsoo_oppa(self):
#         print("instance method 입니다.")

# ClassName()

# class Student: # 클래스 정의
#     def __init__(self, name, ban): # 생성자
#         self.name = name # 인스턴스 변수
#         self.ban = ban

#     def introduce(self): # 인스턴스 메서드
#         print(f"안녕하세요. 저는 {self.ban} {self.name} 입니다.")

# shinyoung = Student("신영", "학생")
# shinyoung.introduce()

# class Example:
#     def __init__(self, value):
#         self.value = value
#     def increment(self):
#         print(self.value)
#         self.value += 1
# exam = Example(10)
# exam.increment()

# exam.increment()
# print(exam)

# class Calculator:
#     def __init__(self, result = None):
#         if not result:
#             self.result = 0 
#         else:
#             self.result = result
#         print(f"{self.result} 값으로 초기화 되었습니다.")

#     def add(self, num): # 5를 받아서
#         self.result += num # self.result = 5를 가산했다.
#         print(self.result)

#     def sub(self, num):
#         self.result -= num # self.result를 5 감산한다.
#         print(self.result)

#     def mul(self, num):
#         self.result *= num
#         print(self.result)

#     def reset(self, num=None):
#         if num:
#             self.result = num
#         else:
#             self.result = 0
#         print(f"{self.result} 값으로 초기화 되었습니다.")    
        
# calc = Calculator()
# calc.add(5)
# calc.sub(2)
# calc.mul(17)
# # calc.reset(167)
# calc = Calculator(100)
# calc.add(5)

"""
ATM 클래스 돈을 입금할 수도 출금 할 수도
입금과 출금시 현재 남아있는 돈이 출력 되도록
출금시 잔액이 부족하면 돈이 없다고 출력
"""

# class Atm:
#     def __init__(self, result = None):
#         if not result:
#             self.result = 0
#         else:
#             self.result = result
#         print(f"{self.result} 값으로 초기화 되었습니다.")

#     def add(self, num): # 5를 받아서
#         self.result += num # self.result = 5를 가산했다.
#         print(self.result) 


#     def out(self, num): # 5를 받아서
#         self.result -= num # self.result = 5를 가산했다.
#         print(self.result)

#     def my(self, num=None):
#         if self.result >= num:
#             self.result -= num
#             print(f"{self.result} 통장 잔고...") 
#         else:
#             print(f"잔액부족 당신의 잔액은 {self.result}...")
#         return    

# my_atm = Atm()
# my_atm.add(10)
# my_atm.out(3)
# my_atm.my(0)

"""
직원 관리 프로그램
직원이 입사하면 회사 전산망에 직원의 사번과 이름, 부서, 연락처를 작성하는 클래스
내용은 딕셔너리로 저장되고 /home/rapa/My_Python/json/result.json 이라는 파일로 백업
직원이 일을 잘하면 연봉을 올려주고, 일을 못하면 자를 수도
객체지향을 고려해 스크립트 작성
"""
from datetime import datetime
import random
import json
import os

class result_manage:
    def __init__(self, name, number, depart, phone, result = None):
        self.name = name
        self.number = number
        self.depart = depart
        self.phone = phone
        self.json_path = "employee.json" # 단어장 파일의 저장 위치를 지정합니다


        if not result:
            self.result = 100
            print(f"당신의 기본 월급은 {self.result}입니다.")
        else:
            self.result = result
        

        self.manage_list = {}

    def load_list(self):

        if not os.path.exists(self.json_path):
            return {}
        
        with open(self.json_path, "r", encoding='utf-8') as file:
            return json.load(file) #  

    def save_list(self):
        with open(self.json_path, "w", encoding='utf-8') as file: #파일을 쓰기 모드로 열어 저장할 준비를 합니다
            json.dump(self.manage_list, file, ensure_ascii=False, indent=4)
    

    def join(self): 
        print(f"이번에 입사한 직원은 {self.name}/{self.number}/{self.depart}/{self.phone}")
        self.temp_dict = {}
        self.temp_dict["name"] = self.name
        self.temp_dict["pay"] = self.result
        self.temp_dict["depart"] = self.depart
        self.temp_dict["phone"] = self.phone
        self.manage_list[275097] = self.temp_dict
        print (self.manage_list)

    def add(self, num):
        if self.temp_dict["name"] == "이신영":
            self.result += num 
            self.temp_dict["pay"] = self.result
            print(f"{self.name}님은 회사에 필요한 인재! 월급은 {self.result}로 상향 되었습니다.") 

    def minus(self, num):
        if self.temp_dict["name"] == "이신영":
            self.result -= num 
            self.temp_dict["pay"] = self.result
            print(f"일을 너무 못했군요...{self.name}님은 월급은 {self.result}로 감봉 되었습니다.") 

    def reset(self, num=None):
        if self.result >= num:
            self.result = num
        else:
            self.result = 0
        print(f"{self.result} 값으로 초기화 되었습니다.")  

result = result_manage("이신영", "C275097", "Pipeline TD", "010-6440-2313")
result.join()
result.add(10)
result.minus(1)
# result.save_list()
result2 = result_manage("솜이 귀여워", "C999999", "Cat", "010-1234-1234")
result2.join()
result2.add(10)
result2.minus(1)
result2.save_list()
result.save_list()
print(result.manage_list)
print(result2.manage_list)