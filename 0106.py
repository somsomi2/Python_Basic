"""
신나는 영어단어 사전 만들기

add를 입력하면 단어 추가 모드가 실행됩니다.
영어 단어와 뜻을 입력할수 있도록 만들어 주세요.

edit을 입력하면 단어 수정 모드가 실행됩니다.
수정할 단어를 입력하면 뜻을 수정할 수 있도록 해주세요.

delete를 입력하면 단어 삭제 모드 입니다.
입력한 단어를 삭제할수 있도록 해주세요.

모든 단어의 뜻과 내용은 딕셔너리에 저장될수 있도록 해주시고,
프로그램을 종료할때 json 파일로 내보내주세요.
프로그램을 다시 시작할때 해당 json 파일을 불러와서 입력했던 영어 단어들이
유지될수 있도록 해주세요.

game을 입력하면 게임 모드가 실행되는데,
저장된 단어가 3개 이상일때 실행될 수 있도록 해주세요.
실행이되면 저장된 단어들중 랜덤으로 단어가 출력되고
해당 단어의 뜻을 입력할수 있도록 해주세요

각 문제를 틀리면 단어의 뜻을 출력해서 공부할수 있도록 해주세요.
문제는 총 3개가 출력되도록 해주시고,
3개를 모두 맞추면 100점 2개를 맞추면 70점 1개를 맞추면 30점이 출력되도록 해주세요

문제를 하나도 맞추지 못하면 사용자가 굴욕적일 수 있는 말을 출력해서
사용자의 학습 의욕을 자극할 수 있도록 해주세요

"""
# import os #os 모듈 호출
# import json #json 모듈 호출
# import random

# def load_json():
#     json_path = "English_dictionary.json"
#     if not os.path.exists(json_path):
#         English_dictionary = {}
#         return English_dictionary
#     with open(json_path, "r") as file:
#         eng_dict = json.load(file)
#     return eng_dict

# def write_json(English_dictionary):
#     json_path = "English_dictionary.json"
#     with open(json_path, "w", encoding='utf-8') as file:
#         json.dump(English_dictionary, file, indent=4, ensure_ascii=False)

# def add_mode(English_dictionary):
#       word = input("영어단어를 입력해주세요. : ")
#       mean= input(f"{word}의 뜻을 입력해주세요. : ")   
#       if not English_dictionary.get(word):
#           English_dictionary[word] = mean     

# def edit_mode(English_dictionary):
#       word = input("수정할 단어를 입력해주세요. : ")
#       mean= input(f"{word}의 뜻을 입력해주세요. : ")
#       if word in English_dictionary:
#           edit_word= input(f"수정하여 입력해주세요. : ") 
#           English_dictionary[word] = edit_word 

# def delete_mode(English_dictionary):
#       delete_word = input("삭제할 단어를 입력해주세요. : ")
#       if delete_word in English_dictionary:
#           del English_dictionary[delete_word]
#       else:
#           print("그런 단어 없심.")      

# def game_mode(English_dictionary):
#     count = 0

#     if len(English_dictionary) > 3:
#         print("3개 이상 단어 필요하심")
#         return
#     words = list(English_dictionary.keys())
#     words = random.sample(words, 3)
#     print ("게임이 시작됩니다.")
#     for word in words:
#         print(f"{word}의 뜻은 무엇일까요?")
#         answer = input("정답은? : ")
#         if answer == English_dictionary[word]:
#             count+=1
#         else:
#             print(f"틀렸습니다. 정답은 {English_dictionary[word]} 입니다.")
        
#     if count == 3:
#         print("100점")
#     elif count == 2:
#         print("70점")
#     elif count == 1:
#         print("30점")
#     elif count == 0:
#         print("0점")
#     return count
                                 
# English_dictionary = load_json()
# while True:
#     base_mode = input("원하는 모드를 입력해주세요. ('add', 'edit', 'delete', 'game', 'exit')")
#     if base_mode == "add":
#         add_mode(English_dictionary)
#     elif base_mode == "edit":
#         edit_mode(English_dictionary)
#     elif base_mode == "delete":
#         delete_mode(English_dictionary) 
#     elif base_mode == "game":  
#         game_mode(English_dictionary)   
#     elif base_mode == "exit":  
#         write_json(English_dictionary)
#         break

"""
집합
파이썬에서 집합은 고유한 요소의 모음입니다.
집합의 목적은 단일 변수에 여러 항목을 저장하는 것 입니다.

특징
- 순서가 없습니다.
- 중복은 허용하지 않습니다.
- 요소는 변경 불가능한 자료형만 사용할 수 있습니다.

집합, 튜플, 리스트, 딕셔너리

"""

# # 집합을 선언하는 방법
# set_1 = set()
# print(type(set_1))

# # 가장 많이 쓰는 방법은 리스트를 set으로 초기화 합니다.
# set_2 = set([1, 2, 3, 4, 5])

# # {}를 이용해서 선언하는 방법
# set_3 = {1, 2, 3, 4, 5}

# # 인덱스와 값을 출력하고 싶으면 반복문과 enumerate를 사용한다.
# for idx, value in enumerate(set_2):
#     if idx == 2:
#         print(idx, value)

# #집합에 요소를 추가 할때
# set_2.add(6) #add 명령어는 집합에 하나의 요소씩 추가할때
# set_2.update([7, 8, 9]) # update는 여러개의 요소를 추가할때 리스트 형식으로

# # 집합에 요소를 지울때
# set_2.remove(9) # 단일 요소를 삭제하나 요소가 없으면 에러남
# set_2.discard(10) # remove와 동일하나 요소가 없어도 에러가 나지 않음 (없으면 안지우고 있으면 지우고)
# pop_item = set_2.pop() # 값의 왼쪽에서부터 삭제(요소중 아무거나 삭제된다고 정의됨)
# print (pop_item)
# print (set_2)

# # 합집합
# # 합집합은 union() 또는 "|" 연산자를 이용합니다.
# baguni_a = {"apple", "banana", "melon"}
# baguni_b = {"water_melon", "papaya", "banana"}

# result = baguni_a.union(baguni_b)
# result = baguni_a | baguni_b #.union과 동일하게 사용가능
# print(result)

# # 교집합
# # 두 집합의 공통인 요소만 포함하는 집합을 만든다.
# # intersection 또는 "-" 연산자를 사용한다.
# result = baguni_a.intersection(baguni_b)
# result = baguni_a - baguni_b

# # 차집합
# # 차집합은 한 집합에는 있지만, 다른 집합에는 없는 요소를 포함하는 집합
# # symetric_difference 또는 "^" 연산자를 사용한다
# result = baguni_a.symmetric_difference(baguni_b)
# result = baguni_a ^ baguni_b

# student_a = {"Junsu", "Serin", "Jaegeon", "Ari", "Nayeon"}
# student_b = {"Seonil", "Hyeogmin", "Nayeon", "Yena", "Ari", "Jaegeon" }
# result = student_a & student_b
# print(f"출석 & 과제 모두 제출한 사람{result}")

# result2 = student_a ^ student_b
# print(f"출석 & 과제 중 하나만 제출한 사람{result2}")

"""
os 모듈은 운영 체제와 상호작용하기 위한 표준 라이브러리
파일 및 디렉토리 작업, 환경 변수 접근 등이 가능하다.

import os # 스크립트 가장 상단에 os 모듈을 불러오는 명령어를 선언하면 사용이 가능하다.

import os
"""
import os
path = "/home/rapa/My_Python/My_Python0106/make_folder"
path2 = "/home/rapa/My_Python/My_Python0106/make_folder/1/2/3/4/5/6/7"

# os.mkdir(path) #파일을 하나씩 만들때
# os.makedirs(path2) #파일을 여러개씩 만들때

print (os.listdir("/home/rapa")) #존재하는 파일 속 보기
print(os.path.exists("/home/rapa/hahaha")) #파일이 존재하는지 찾아보기

# # 디렉토리 작업
# os.mkdir(path) #디렉토리를 생성한다.
# os.makedirs(path) # 입력된 모든 경로의 폴더를 생성한다.
# os.rmdir(path) # 입력된 경로의 디렉토리를 삭제한다.
# os.listdir(path) #경로상의 모든 폴더와 파일을 리스트로 반환한다.

# # 파일 작업
# os.remove(path) # 경로상의 파일을 삭제한다.
# os. rename(src, dst) # src 경로의 파일을 dst 경로의 이름으로 변경한다.

# # 경로 관련
# os.path.join(path, path) # 2개의 패스를 하나의 경로로 생성합니다.
# os.path.dirname(path) # 디렉토리 경로를 반환한다.
# os.path.basename(path) # 경로에서 파일의 이름을 반환한다.
# os.path.exists(path) # 파일 또는 디렉토리가 존재하는지 확인한다(True or False)
# os.path.splitext(path) # 파일 이름과 확장자를 리스트로 분리하여 반환한다.

# 프로세스
# os.getpid() # 현재 프로세스 id를 가져온다.
# os.getlogin() # 현재 로그인 사용자의 이름 가져오기

