"""
제귀함수
함수가 스스로를 호출하는 함수
특정 조건이 완료되면 제귀하지 않는 명령이 필수적

def 함수명(매개변수):
    if 조건이 완료되면
        함수종료
    명령어
    return 함수명(매개변수)
"""

# 10을 매개변수로 전달해서 함수를 실행했을때,
# 1씩 감소하며 제귀함수가 호출되고 0이 되었을때 멈춘다.

# def recursive_func(number):
#     if number == 0:
#         print("마침내 0이 되었군.")
#         return
    
#     number -= 1
#     print(number)
#     return recursive_func(number)

# recursive_func(10)

# 함수가 실행될때마다 숫자가 1씩 줄어들고, 그값들이 리스트에 추가되는 함수
# my_list = []
# def recursive_func(number):

#     if number == 0:
#         print("마침내 0이 되었군.")
#         return
    
#     number -= 1
#     my_list.append(number)
#     return recursive_func(number)

# recursive_func(10)
# print(my_list)

# 재귀함수 사용식
def recursive_append(number, result=None):

    if result is None: # 리스트가 없으면 리스트를 만들기 위해 작성한 조건문
        result = []

    if number == 0: # 재귀함수 종료 조건 선언
        return result
    
    number -= 1 # 1을 감산하고
    result.append(number) # result 리스트에 값 넣기

    return recursive_append(number, result)
result = recursive_append(11)
print(result)


