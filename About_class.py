# class Student:
#     def __init__(self, name, age):
#         self.name = name #self란 인스턴스 내부에서 사용할수 있는 함수
#         self.age = age

#     def set_name(self):
#         print(self.name) 

#     def set_age(self, age):
#         print(f"{self.age}가 {age}로 변경되었습니다.")
#         self.age = age    
   

#     pass

# stu1 = Student("신영", 23)
# stu1.set_age(30)

# print(stu1.name)
# print(stu1.age)


# class Student:
#     def __init__(self, name, age):
#         self.name = name #self란 인스턴스 내부에서 사용할수 있는 함수
#         self.age = age

#     def set_name(self):
#         print(self.name) 

#     def set_age(self, age): #인스턴스 메서드
#         print(f"{self.age}가 {age}로 변경되었습니다.")
#         self.age = age   

#     @staticmethod # 정적 메서드
#     def add_parameter(num1, num2):
#         """클래스, 인스턴스에 영향을 주지 않고 독립적인 역할을 수행하는 함수"""
#         result = num1 + num2
#         print(f"{num1} + {num2}의 값은 {result} 입니다.")
#         return result
#     def __str__(self): # 매직 메서드
#         """인스턴스를 print로 실행 했을때 출력되는 문자열 메서드"""
#         return(f"안녕하세요 {self.name} 입니다. 나이는 {self.age}입니다.")   
#     pass

# stu1 = Student("신영", 23)
# stu1.set_age(30)
# stu1.add_parameter(5, 6)
# print(stu1)

"""고용 프로그램 만들기"""
from datetime import datetime
import random
import json
import os

class VFX_EmployeeManager:

    def __init__(self):
        """
        VFX 직원 관리 소프트웨어 입니다.
        """
        print("VFX 직원 관리 소프트웨어 입니다.")      
        self.json_path = "/home/rapa/My_Python/My_Python0109/employee_class.json"


        self.employee_dict = self.load_json() #생산자에서 딕셔너리를 추가

        print (self.employee_dict)

        with open(self.json_path, "w") as file:
            json.dump(self.employee_dict, file, ensure_ascii=False)

    def add_employee(self, name, age, phone, dept, pay, exp):
        """구성원을 추가하는 메서드"""
        employee_code = self.get_employee_code()

        #중첩 딕셔너리를 만드는 방법_1
        self.employee_dict[employee_code] = {
            "이름" : name,
            "나이" : age,
            "연락처" : phone,
            "부서" : dept,
            "연봉" : pay,
            "경력여부" : exp
        }
        added_employee_name = self.employee_dict[employee_code]["이름"]
        print(f"{added_employee_name}님이 추가 되었습니다.")
        print("당신의 노동을 기대합니다.")
        self.update_json()
        # 중첩 딕셔너리를 만드는 방법_2
        # tmp = {}
        # tmp["이름"] = name
        # tmp["나이"] = age
        # tmp["연락처"] = phone
        # tmp["부서"] = dept
        # tmp["연봉"] = pay
        # tmp["경력여부"] = exp
        # self.employee_dict[employee_code] = tmp

    def fire_employee(self, name):
        """
        직원을 해고하는 메서드.
        이름을 매개변수로 받고, 해당 이름의 모든 구성원을 출력해서
        사용자가 해당 구성원을 해고할수 있도록 정보를 제공하는 함수
        """
        for employee_code, privacy_dict in self.employee_dict.items():
            employee_name = privacy_dict["이름"]
            if not employee_name == name:
                continue
            dept = privacy_dict["부서"]
            print(f"{employee_code} : {employee_name} - {dept}")

        id = input("해고하려는 구성원 사번을 입력해주세요. : ")
        if id in self.employee_dict:
            answer = input("정말 해고하시겠습니까? (yes/no) : ")
            if answer == "yes":
                del self.employee_dict[id]
                self.update_json()
                
        print(self.employee_dict)

    def get_employee_code(self):
        #날짜를 불러와 사번 만들기 (ex.250110_9614)
        now = datetime.now()
        now_data = now.strftime("%y%m%d")
        random_number = random.randint(1000, 9999) # 랜덤한 사번 부여
        employee_code = f"{now_data}_{random_number}"
        print(employee_code)
        return(employee_code)
        
    def load_json(self):
        """json 파일을 불러오는데, 경로에 없을 경우 빈 딕셔너리를 리턴합니다."""
        if not os.path.exists(self.json_path):
            return{}

        with open(self.json_path, "r") as file:
            data = json.load(file)
        return data
    
    def update_json(self):
        """현재 인스턴스의 사원 딕셔너리를 저장합니다."""
        with open(self.json_path, "w") as file:
            json.dump(self.employee_dict, file, ensure_ascii=False, indent=4)


    
vfx_manager = VFX_EmployeeManager()
vfx_manager.add_employee("이신영", 23, "010-6440-2313", "파이프라인 TD", 5300, "경력")
vfx_manager.fire_employee("이신영")
