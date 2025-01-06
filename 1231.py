# print 명령은 표준 출력을 합니다. (standard out)
#print("Hello World")

#a = "Hello"
#b = "World"
#c = "1" #문자의 형태를 가진 1
#print (a+b+c)

# 파이썬에서 문자열을 생성하는 방법

# text = "Hello World"
# text1 = 'Hello World'
# text2 = """Hello World"""
# text3 = '''Hello World'''
# print (text, text1,text2, text3)


# text = '''"Shinyoung's favorit\n food is"'''
# print (text)

# print("*"*20)
# print(dkfhjaljflkjf)
# print("*"*20)

"""
변수
변수는 데이터를 저장하기 위한 이름
변수는 메모리의 특정 위치에 데이터를 저장하고, 그 데이터를 이름으로 참조할 수 있도록 합니다.
"""
# a = 10 #정수
# b = 3.5 #소수
# c = "python" #문자열

# print(type(a))
# print(type(b))
# print(type(c))

# 변수 이름 규칙
# 문자열 a-z, A-Z, 0-9, _를 이용하여 변수 이름 설정
# 숫자로 시작하지 않게 주의
# 공백을 포함 할 수 없음
# 변수이름은 의미 있게 짓는 것이 좋다

# name = "shinyoung"
# age = "22"
# height = "162"

# print("이름 : ", name)
# print("나이 : ", age)
# print("신장 : ", height)


#  변수 재할당
# x = 10
# print (x)

# x = "python"
# print (x) # 변수는 새로운 값으로 덮어씌워진다

# a, b, c = 1, 2, 3
# print (a, b, c)


# a = "20"
# to_digit = int(a) #매개변수
# to_digit = str(a) #문자열
# print (type(to_digit))

"""
문자열 슬라이싱
"""
#text = "Netflix Academy"
# print (text[0])
# print (text[0]+text[8]) #문자열 더하기도 가능하다
# print (text[0:6]) #0~6번째까지 출력한다 (범위지정 슬라이싱)
# print (text[:: -1]) #문자열 뒤집어서 출력하기


# text = "20241231Sunny"
# year = (text[0:4])
# month = (text[4:6])
# day = (text [6:8])
# weather = (text[8:])
# print (year, month, day, weather)

"""
문자열 포맷팅
"""

# text = "여러분"
# cg = "CG"

# # 1. 더하기 키워드
# print (text + "은" + cg + "가 재밌나요?")

# # 2. % 서식
# print ("%s은 %s가 재미있나요?" % (text, cg))

# # # 3. str.fomat 함수
# print ("{}은 {}가 재미있나요?".format(text, cg))

# # # 4. f 문자열 (f-string)
# print (f"{text}은 {cg}가 재미있나요?")

# # 소수자리 출력

# fi = 3.1415
# print (round(fi, 2))
# print (f"{fi:.2f}")

"""
리스트
list란 Python에서 여러 값을 하나의 변수에 저장 할 수 있는 자료형
리스트는 순서가 있는 컬렉션으로 각요소는 인덱스를 통해 접근 가능
Python에서 리스트는 []로 정의하며 내부의 요소들은 쉼표로 구분

리스트의 특징
1. 순서가 있기에 리스트의 요소는 0부터 시작하는 인덱스를 가진다.
2. 요소는 값 변경, 삭제가 가능
3. 중복이 허용된다
4. 다양한 자료형 저장 가능
"""

# my_list = ["승연님", "준수님", "형민님"]
# my_list.append("주혜님") #append는 리스트의 가장 뒤에 요소를 추가한다
# my_list.insert(1, "예나님") #내가 원하는 인덱스에 요소를 추가한다
# my_list.remove("예나님") #내가 원하는 인덱스 요소를 삭제 할 수 있다.
# #print (my_list[0]) #인덱스로 불러 올 수 있다
# print (my_list)

# aa = my_list.pop(0) #remove 명령어와 동일하나 반환값이 있다
# print (aa) 

# your_list = [3, 2, 4, 5]
# print (your_list.sort(reverse=True)) #오름차순 정렬

""" if문
조건문을 작성할때 사용하는 구문
특정 조건이 참(True)일 때만 실행되는 코드를 작성 가능

기본구문
if 조건:
    실행할 코드

조건식의 비교 연산자
== 값이 같음
!- 값이 다름
> 왼쪽이 더 큼
< 오른쪽이 더 큼
>= 왼쪽이 크거나 같음
<= 오른쪽이 크거나 같음
"""

# my_list = ["승연님", "준수님", "형민님"]
# if "준수님" in my_list:
#     print("준수님이 해당 리스트에 존재합니다.")

# elif "형민님" in my_list:
#     print("형민님이 해당 리스트에 존재합니다.")

# else:
#     print("준수님이 해당 리스트에 없습니다.")

# num = 30
# if num > 10:
#     print("10보다 큽니다.")
# if num >= 10:
#     print("같습니다.")

# 논리 연산자
# and : 조건이 모두 만족해야 조건이 참이 된다
# or : 둘중 하나만 만족되었을때 조건이 참이 된다.
# not : 조건이 거짓일때 실행되도록 한다.

# age = 18
# edu = "중졸"

"""
input() 명령어는 사용자가 프로그램 실행 중 데이터를 입력 할 수 있도록 하는 데 사용됩니다. 
이 명령어는 사용자가 입력한 값을 문자열로 반환합니다.

변수 = input("프롬프트")
"""
# edu = input("최종학력을 입력해주세요. : ")
# age = int(input("나이 입력해주세요. : "))


# if age >= 18 and (edu == "고졸" or edu == "대졸"):
#     print("지원 자격이 있습니다.")  
# else:
#     print("다음 기회에 지원해주세요.")


"""
 반복문 (for)
 For문은 컬렉션을 순회하며 각 요소에 대해 특정작업을 수행 할 떄 사용됨

기본문법
for 변수 in 컬렉션:
    실행할 코드
# 컬렉션 : 반복 가능한 객체 (iterable)로 정의됩니다.
"""
fruits = ["apple", "banana", "mango", "papaya"]

# for idx, fruit in  enumerate(fruits):
#     print (f"나는 {idx} - {fruit} 좋아해요.")

# idx = 0
# for fruit in fruits:
#     print (f"나는 {idx} - {fruit} 좋아해요.")
#     idx += 1

#빠르게 테스트 가능
# for i in range(1, 10, 2): #range(a, b, inc) a : 시작, b : 마지막 -1, 증가값
#     print (i)

# for i in range(2, 9):
#     for j in range(1, 10):
#         result = i * j
        
#         if j == 5: #5일때 if문을 멈추겠다.
#             break

#         print (f"{i}x{j}={result}")


# numbers = [6, 17, 24, 31, 39, 50]
# result = 0

# for number in numbers:
# #do
#     result += number
# #done
# print (result)

# words = ["level", "hello", "python", "radar"]
# palindromes = []

# for word in words:
#     reverse_word = (word[:: -1])

#     if word == reverse_word:
#         palindromes.append(word)
#         #print(palindromes)
#         print(f"로꾸꺼는{palindromes}입니다")


# game_ran = 100
# for game in range(1, game_ran+1):
#         num_369 = str(game)
#         if '3' in num_369 or '6' in num_369 or '9' in num_369:
#             print("짝")
#         else:
#             print(game)
# print(game)

words = ["새해", "건강", "복", "취업", "많이", "진하게", "받으세요"]
result = []
for idx, word in enumerate(words):
    if idx % 2 == 0:
        result.append(word)
result = (" ".join(result))       
print (result)

words = ["새해", "건강", "복", "취업", "많이", "진하게", "받으세요"]
for i in range (0, len(words), 2):
    print (words[i])

i = 0
for word in words:
    if idx % 2 == 0:
        print (word)

for idx, word in enumerate(words):
    if not idx % 2 == 0:
        continue
    result.append(word)