"""
클래스 = 함수들의 집합

추상 클래스란?

추상클래스는 객체지향프로그램에서 사용되는 개념으로, 
반듯이 구현해야하는 메서드를 정의해 놓은 클래스
추상클래스는 실제로 객체를 생성할 수 없으며,
상속받은 클래스가 추상 메서드를 구현해야 생성 가능
"""
"""
추상 클래스를 사용하는 이유
1. 일관성 유지 : 상속 받은 클래스가 특정 메서드를 반듯이 구현해야함
2. 공통 시능 제거 : 중볻된 코드를 줄이고, 기본 동작을 부모 클래스에서 구현해
                    유지보수가 유용
3. 코드의 가독성과 명확성 : 추상 클래스는 "이클래스는 이렇게 동작해야한다.
                           라는 가이드를 제공
"""

# from abc import ABC, abstractmethod
# # Abstract Base Classes

# class Shape(ABC): #쉐입이라는 추상 클래스 ABC를 상속 받음

#     @abstractmethod # 추상클래스를 만들기
#     def draw(self): # 드로우라는 메서드를 꼭 정의하고 사용해야됨
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("원을 그립니다.")

# class Rectangle(Shape):
#     def draw(self):
#         print("사각형을 그립니다.")

# a = Circle()
# print(a)

"""
캡슐화란?
객체 지향 프로그래밍의 중요한 개념 중 하나로,
객체의 데이터와 이를 처리하는 메서드를
외부에서 접근하지 못하도록 제한하는 것
대신 데이터를 간접적으로 조작할 수 있는 인터페이스를 제공

사용하는 이유:
데이터 보호 - 외부에서 객체의 내부 데이터에 직접 접근하여
잘못된 데이터를 입력하거나, 설정하여 의도치 않는 변경을 방지 하기 위해.

데이터 무결성 보장

내부 로직은 감추고, 필요한 부분만 외부에 노출함으로써
객체의 사용방법이 단순해지고 명확해진다.
"""

#캡슐화를 사용하지 않은 클래스
# class CrazyArcade(10000):
#     def __init__(self, cache):
#         self.cache = cache

#캡슐화를 사용한 클래스
# class CrazyArcade:
#     def __init__(self, cache):
#         self.__cache = cache # 비공개 속성
#         # _ : 따로 가능은 없으나, 클래스 내부에서만 조회 및 편집이 가능하도록 개발자들간의 약속
#         # __ : 외부에선 접근할 수 없도록 설정

#     # def _set_cache(self):
#     #     self._cache

#     def add_cache(self, cache):
#         if cache < 0:
#             print("0보다 작은수는 충전될수 없습니다.")
#             return
#         self.__cache += cache
#         print ("충전이 완료되었습니다.")
#         print ("잔액", self.__cache)
# 준수 = CrazyArcade(10000)
# 준수.add_cache(30)

# 함수의 캡슐화를 사용한 클래스
# class CrazyArcade:
#     def __init__(self, cache):
#         self.__cache = cache # 비공개 속성
#         # _ : 따로 가능은 없으나, 클래스 내부에서만 조회 및 편집이 가능하도록 개발자들간의 약속
#         # __ : 외부에선 접근할 수 없도록 설정

#     def call__add_cache(self, cache):
#         self.__add_cache(cache)

#     def __add_cache(self, cache):
#         if cache < 0:
#             print("0보다 작은수는 충전될수 없습니다.")
#             return
#         self.__cache += cache
#         print ("충전이 완료되었습니다.")
#         print ("잔액", self.__cache)

# 준수 = CrazyArcade(10000)
# 준수.call__add_cache(30)

"""
예외처리란?
예외란? 프로그램 실행 중 발생하는 오류를 의미.
예외는 프로그램을 중단시키지만, 예외처리를 통해
이를 제어하고, 프로그램이 계속해서 실행되도록 할 수 있습니다.

기본구문
try:
    # 예외가 발생할 가능성이 있는 코드
except 예외타입(선택)
    # 예외 발생시 실행되는 코드
else:
    #예외가 발생하지 않으면 실행되는 코드 (선택적)
finaly:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
"""

# for i in range(0, 10):
#     try: 
#         f = open("/home/rapa/My_Python/amoogerna.text")
#     except:
#         print ("경로에 파일이 없는거 같아요. 경로를 확인해주세요")
#         print(i)

# # 각각의 예외에 따라서도 다르게 설정을 할수가 있다.
#     try: 
#         result = 10/0
#     except ZeroDivisionError as e:
#         print(e)
#         print ("0으로 나눌 수 없습니다.")
#     except TypeError as e:
#         print(e)
#         print("잘못 입력하셨습니다.") 

# else : 예외가 발생하지 않았을때 실행됨
# try:
#     result = 10/3
# except ZeroDivisionError:
#     print("0으로 나눌 수 없음")
# else:
#     print(f"계산 결과 {result}")

# finaly : 예외가 발생하지 않았을때 실행됨
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없음")
# finally: # 되던말던 무조건 출력함 / 사용을 지양할 것(위험한 코드)
#     print(f"계산 결과")

# 숫자만 나오게 만들기
data_list = ["10", "20", "good"]
new_list = []
for text in data_list:
    try:
        result = int(text)
    except:
        print(f"{text}는 숫자가 아니에용")
        continue
    new_list.append(result)
print(f"{new_list}")

# 모든 예외를 포괄적으로 처리하는 Exception 명령어
try:
    result = 10/ int(input("숫자를 입력해주세요. : "))
except Exception as e:
    print(f"예외가 발생했어요 ~~ : {e}")