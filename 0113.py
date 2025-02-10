
# class Student:

#     index = 0 # 클래스 변수
#     """
#      클래스 변수는 클래스 전체에서 공유되는 변수.
#      모든 인스턴스가 동일한 값을 참조
#      클래스 정의 부분에 선언되고, 특정 인스턴스가 아니라, 클래스 자체에 속한다.
#     """

#     def __init__(self, name, age=None): # age=None은 인스턴스 변수가 비어있어도 넘어가도록 한다.
#         """생성자"""
#         self.name = name

#         if age is None:
#             self.age = "비밀"
#         else:
#             self.age = age

#         Student.index +=1 # 클래스명.변수명으로 클래스 변수에 접근

#     def annyeonghaseyo(self):
#         """
#         나를 소개하는 메서드
#         2개의 인스턴스 변수를 사용해서
#         나를 소개하는 문자열을 표준출력하는 함수.
#         """
#         print(f"저는 {self.name}이고, 나이는 {self.age}입니다.")
# std1 = Student("준수", 25)
# std2 = Student("도은")
# std2.annyeonghaseyo()

# class Academy(Student): # Student 클래스를 상속 받겠습니다.
    
#     def __init__(self, name, age=None):
#         super().__init__(name, age) # 부모 클래스의 생성자를 호출하겠다.
#         # self.annyeonghaseyo()

#     def annyeonghaseyo(self):
#         super().annyeonghaseyo() # 이 문장 주석처리시 앞으로 잘부탁드리겠습니다 내용만 나오게됨
#         print("앞으로 잘 부탁드리겠습니다.")

# std1 = Academy("형민", 25)
# std2 = Academy("도은")
# print(std2.index)
# std3 = Academy("준수", 28)
# print(std3.index)

# print(Academy.index) # 클래스명.변수 or 객체명.변수로 클래스 변수에 접근 가능

# # std1.annyeonghaseyo()
# # print(type(Academy))
# # print(Academy)

# help(Student) #주석처리된 내용을 정리되어 볼수 있다.


"""
캐릭터라는 부모 클래스를 상속 받습니다.
Wizard, Warrior, Archer 등의 자식클래스를 만들어
부모클래스가 가진 attack_damage 메서드에서 선언된 self.base_damage를
각 직업에 맞는 공격력으로 구할수 있도록 메서드 오버라이트
스크립크를 실행하면 3개의 객체를 만들고 반복문으로
캐릭터들의 attack_damage() 메서드를 실행할수 있도록 해주시고,
damage가 각 캐릭터 이름과 함께 출력되게 해주세요.

워리어:
기본 공격 대미지 2배
10% 확률로 대미지 2배

마법사:
기본 공격 대미지 1.5배
30% 확률로 대미지 2배

아처:
50% 확률로 대미지 3배
"""

import random
random.random() < 0.3

class Charecter:

    def __init__(self, name):
        self.name = name
        self.base_damage = 10

    def attack_damage(self):
        """
        기본 공격 대미지
        (자식 클래스에서 오버라이딩 필요)
        """
        return self.base_damage
    
class Warrior(Charecter):
    """워리어"""
    def attack_damage(self):
        damage = self.base_damage *2 
        print(f"대미지: {damage}")
        if random.random() < 0.1:
            damage *= 2
            print(f"{self.name}의 기술") 

class Wizard(Charecter):
    def __init__(self, name):
        super().__init__(name)
    
    """위자드"""
    def attack_damage(self):
        damage = self.base_damage *1.5
        print(f"대미지: {damage}")
        if random.random() < 0.3:
            damage *= 1.5
            print(f"{self.name}의 기술")    

class Archer(Charecter):
    """아처"""
    def attack_damage(self):
        damage = self.base_damage
        print(f"대미지: {damage}")
        if random.random() < 0.5:
            damage *= 3
            print(f"{self.name}의 기술")          

chr1 = Archer("신영")
chr1.attack_damage()

