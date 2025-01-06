# 계산기 만들기

# result = 0 # boolean 자료형 이어서 조건식에서 참/거짓으로 표현가능

# while True:
#     if not result:
#         user_input = input("숫자와 연산자 숫자를 순서대로 입력해주세요. : ")
#     else:
#         user_input = input(f"현재 값은 {result} 입니다. 다음 계산을 입력해주세요 : ")


#     if user_input == "exit":
#         print("계산기를 종료합니다.")
#         break
#     if user_input == "clear":
#         print("계산기를 초기화합니다.")
#         result = 0
#         continue

#     if not result:
#         num1, operator, num2 = user_input.split()
#         num1, num2 = float(num1), float(num2)
#         result = num1
#     else:
#         operator, num2 = user_input.split()
#         num2 = float(num2)
    
#     if operator == "+":
#         result += num2
#     elif operator == "-":
#         result -= num2
#     elif operator == "*":
#         result *= num2    
#     elif operator == "/":
#         result /= num2  

#     # 자리수 처리
#     if result.is_integer():
#         result = int(result)
#     else:
#         result = round(result, 2)


# original_list = [1, 2, 3]
# my_list = original_list

# my_list.append(4)

# from copy import copy #원본 값에는 영향을 주지 않게 복사해놓는다.
# c = copy(original_list)

# c.append(5)

# print (id(original_list))
# print (id(my_list))
# print (id(c))

# #딕셔너리 선언 방법 1
# user_profile = {"name":"shin", "age":23, "addr":"busan"}
# print (user_profile)

# #딕셔너리 선언 방법 2
# user_profile2 = {}
# user_profile2["name"] = "shin"
# user_profile2["age"] = "23"
# user_profile2["addr"] = "busan"
# print(user_profile2)

# print (user_profile.keys()) #key값들을 출력함
# print (user_profile.values()) #values값들을 출력함

# #key와 value 한번에 출력
# for key, value in user_profile.items():
#     if key == "name":
#         print (key, value)

# # print (user_profile["phone"]) phone이라는 딕셔너리가 존재하지 않아 에러
# user_profile = {"name":"shin", "age":23, "addr":"busan"}
# user_profile.get("phone") #그냥 넘어가는 코드
# phone_key = user_profile.get("phone") #폰의 키를 추가하는 코드
# if not phone_key:
#     user_profile["phone"] = "010-1234-1234"
# print(id(phone_key))

# phone_key = user_profile.get("phone")
# if phone_key:
#     user_profile["phone"] = "010-7774-7777"

# del user_profile["phone"] #키 값 삭제하기
# print(user_profile)


# student_dict = {}
# grade_dict = {}

# grade_dict["kor"] = 65
# grade_dict["eng"] = 60
# grade_dict["math"] = 62
# student_dict["seonil"] = grade_dict.copy()

# grade_dict["kor"] = 70
# grade_dict["eng"] = 40
# grade_dict["math"] = 50
# student_dict["shinyoung"] = grade_dict.copy()

# for key, value in student_dict.items():
#     total = sum(value.values()) #sum 명령어를 사용하면 리스트의 요소들을 더한 값을 알 수 있다.
#     count = len(value) #len 명령어를 사용하면 리스트의 요소 갯수를 알 수 있다.
#     result = total / count
#     print(f"{key}님의 총점은 {total}, 평균은 {result} 입니다.")     

"""
JSON파일로 내보내기
python의 json 모듈을 이용해서 딕셔너리를 파일로 저장 할 수 있다.
"""
# import json #JSON 데이터를 다루기 위한 모듈불러오기

# #딕션너리를 JSON 데이터로 컨버팅하여 파일 내보내기
# # indent=4 : 파일을 보기 좋게 설정한다.
# # ensure_ascii : 아스키코드 형태로 보지 않겠다.
# with open("/home/rapa/My_Python/My_Python0103/json/student_dict.json","w") as file:
#     json.dump(grade_dict, file, indent=4, ensure_ascii=False)

# #JSON 파일을 불러와서 DICTIONARY형태로 저장하기
# with open("/home/rapa/My_Python/My_Python0103/json/student_dict.json","r") as file:
#     loaded_dict = json.load(file)
# print (loaded_dict)

"""
함수
함수란 반복적으로 작성되는 코드 중에서 반복적 사용의 가치와 사용률이 높은 부분을 하나의 그룹으로 묶어
입력 값에 따라 결과값을 반복 시켜주는 것

기본 사용 구분: #매개변수와 인자는 없어도 됨
def 함수이름 (매개변수):
    명령어

함수이름(인자)
"""

# 기본적인 함수

# def hello():
#     """
#     이 함수가 호출(실행)되면 world라는 문자열이
#     표준 출력되는 함수 입니다.
#     """
#     print("world")

# hello() # 정의한 함수를 호출하는 명령어

# # 반환값(리턴값)이 있는 함수.
# def add():
#     result = 1 + 2
#     return result

# value = add()
# print (value)

# # 리턴 명령어로 함수 종료하기
# def junsoo():
#     return # 함수를 종료시킬때도 사용될수 있다
#     print("준수님은 사실 천재여씀")
# junsoo()

# # 리턴이 여러개인 함수( 명확하지 않은 함수 이기에 사용 지양 )
# def test_return():
#     return 1, 2, 3
# value = test_return() # 튜플의 형태로 데이터가 반환된다.
# print(value)

# v1, v2 ,v3 = test_return() # 리턴의 개수가 정의 되어 있다면
# print(v1, v2, v3)

# # 매개변수를 사용하는 함수
# def test_variable(a, b): # a, b를 매개 변수라고 이야기 한다.
#     """
#     이 함수는 2개의 매개변수가 필요하고
#     입력받은 매개변수를 곱한 값을 리턴하는 함수이다.
#     """
#     result = a * b
#     return result

# # 매개변수를 미리 초기화 하는 함수
# # 오른쪽 매개 변수부터 초기화가 가능하다.
# def test_variable(a, b = 6): # 1, 2 변수를 인자라고 이야기 한다.
#     """
#     이 함수는 2개의 매개변수가 필요하고
#     입력받은 매개변수를 곱한 값을 리턴하는 함수이다.
#     """
#     result = a * b
#     return result

# value = test_variable(3)
# print (value)

# # 인자가 여러개일때
# # 확실하지 않은 데이터의 처리 방식 사용 지양
# def test_args(*shinyoung):
#     print (shinyoung)
# test_args(1, 2, 3, 4, 5)

# def get_add(num1, num2):
#     return num1 + num2

# value = get_add(3, 6)
# print (value)

# def gugudan(num):
#     for i in range(1, 10):
#         result = num * i
#         print (f"{num} x {i} = {result}")
        
# for i in range(2, 10):
#     gugudan(i)

# def exchange_rate(k = 1000, u = 1467, n = 932):
#     result  = k / u
#     result_1  = k / n    
#     return result, result_1
# value, value2 = exchange_rate(int(input("환전 금액을 입력해주세요:) : ")))
# print (f"환전 금액은 달러{value:.2f} 엔화{value2:.2f}입니다")

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print((A%C)*(B%C)%C)


# num1 = int(input())
# num2 = input()

# print(num1*num2[2])
# print(num1*num2[1])
# print(num1*num2[0])
# print(num1*num2)

# total = 0
# A, B, C = input()
# total = int(A) + int(B) + int(C)
# print(total)


user_profile = {
    "강백호": {
        "학교": "북산고등학교",
        "포지션": "포워드",
        "키": 190,
        "특징": [
            "농구 초보",
            "자신감 넘침",
            "운동신경 뛰어남"
        ]
    },
    "서태웅": {
        "학교": "북산고등학교",
        "포지션": "포워드",
        "키": 187,
        "특징": [
            "냉철함",
            "천재 농구 선수",
            "여학생들에게 인기 많음"
        ]
    },
    "송태섭": {
        "학교": "북산고등학교",
        "포지션": "가드",
        "키": 168,
        "특징": [
            "빠른 스피드",
            "작은 키",
            "경기 조율 능력"
        ]
    },
    "채치수": {
        "학교": "북산고등학교",
        "포지션": "센터",
        "키": 197,
        "특징": [
            "리더십",
            "성실함",
            "팀 주장"
        ]
    },
    "정대만": {
        "학교": "북산고등학교",
        "포지션": "가드",
        "키": 184,
        "특징": [
            "3점 슛의 달인",
            "거친 과거",
            "성숙한 모습"
        ]
    },
    "윤대협": {
        "학교": "능남고등학교",
        "포지션": "포워드",
        "키": 190,
        "특징": [
            "능남의 에이스",
            "침착함",
            "경기 흐름을 읽는 능력"
        ]
    },
    "신현철": {
        "학교": "능남고등학교",
        "포지션": "센터",
        "키": 200,
        "특징": [
            "압도적인 피지컬",
            "리바운드 강점",
            "골밑 플레이"
        ]
    },
    "이정환": {
        "학교": "해남고등학교",
        "포지션": "가드",
        "키": 178,
        "특징": [
            "완벽한 경기 운영",
            "냉정함",
            "경기 전체를 컨트롤"
        ]
    },
    "김수겸": {
        "학교": "해남고등학교",
        "포지션": "포워드",
        "키": 188,
        "특징": [
            "팀워크 중시",
            "공수 밸런스 좋음",
            "꾸준함"
        ]
    },
    "황태산": {
        "학교": "풍산고등학교",
        "포지션": "가드",
        "키": 183,
        "특징": [
            "강한 정신력",
            "투지 넘침",
            "거친 플레이"
        ]
    }
}
# # 문제 1번
# for key, value in user_profile.items():
#      if key == "윤대협":
#           school = value["학교"]
#           position = value["포지션"]
#           height = value["학교"]
#           charactor = value["학교"]
#           print (f"{key}의 정보")
#           print (f"학교:{school}")          
#           print (f"포지션:{position}")             
#           print (f"키:{height}")
#           print (f"특징:{charactor}")

# 문제 2번
# school_list = ["해남고등학교","풍산고등학교", "능남고등학교", "북산고등학교"]
# print(f"등장 학교들:")
# for school in school_list:
#     if school == "해남고등학교":
#          print(f"{school}")
#     if school == "풍산고등학교":
#          print(f"{school}") 
#     if school == "능남고등학교":
#          print(f"{school}") 
#     if school == "북산고등학교":
#          print(f"{school}")          
# else:
#     school_list.append(school) 

# 문제 3번 
# school_profile = {}
# school_profile["school"] = "능남고등학교"
# school_profile["yun"] = "윤대협","(포워드)"
# school_profile["shin"] = "신현철","(센터)"
# for key, value in school_profile.items():
#     if key == "school": 
#         print(f"{value}의 선수들:") 
#     if key == "yun": 
#         print(f"{value}")   
#     if key == "shin": 
#         print(f"{value}")  

# print ("능남고등학교의 선수들")
# for key, value in user_profile.items():
#     school = value["학교"]
#     if school == "능남고등학교":
#         print (key, value["포지션"])


# 문제 4번
# school_info = {}
# for key, value in user_profile.items(): 
#     school = value["학교"] [:2]
#     if not school_info.get(school):
#         school_info[school] = []
#     school_info[school].append(key)

# for key, value in school_info.items(): 
#         print (f"{key}: {' ,'.join(value)}") 
  
# 문제 5번
# print ("키가 190 이상인 선수들:")
# for key, value in user_profile.items():
#     height = value["키"]
#     if height >= 190:
#         school = value["학교"]
#         print(f"{key}({school},{height})")


# 문제 6번
# print ("포지션별 선수: ")
# for key, value in user_profile.items():
#     position = value["포지션"]  
#     if position == "포워드":
#         print(f"포워드: {key} ")
#     if position == "가드":
#         print(f"가드: {key} ")
#     if position == "센터":
#         print(f"센터: {key} ")  


# print ("포지션별 선수: ")
# student_info = {}
# for key, value in user_profile.items():
#     position = value["포지션"]
#     if not student_info.get(position):
#         student_info[position] = []
#     student_info[position].append(key)

# for key, value in student_info.items():
#     print (f"{key}: {', '.join(value)}")     

# import json
# with open("/home/rapa/My_Python/My_Python0103/json/slamdunk.json", "r") as file:
#     loaded_dict = json.load(file)

# for key, inner_dict in user_profile.items()
# if key == "윤대협":
#     print(inner_dict)
    
#     school = inner_dict["학교"]



