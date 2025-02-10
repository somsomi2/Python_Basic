from datetime import datetime
import random
import json
import os

class result_manage:
    def __init__(self):
        self.json_path = "employee_re.json" # 단어장 파일의 저장 위치를 지정합니다
        self.employee_dict = self.load_json()

    def load_list(self):

        if not os.path.exists(self.json_path):
            return {}
        
        with open(self.json_path, "r", encoding='utf-8') as file:
            return json.load(file) #  

    def save_list(self):
        with open(self.json_path, "w", encoding='utf-8') as file: #파일을 쓰기 모드로 열어 저장할 준비를 합니다
            json.dump(self.manage_list, file, ensure_ascii=False, indent=4)
    

    def add_employee(self, name, age, phone, dept, pay, exp): 
        employee_code = self.get_employee_code()

        # 중첩 딕셔너리를 만드는 첫번째 방법
        self.employee_dict[employee_code] = {
            "이름" : name,
            "나이" : age,
            "연락처" : phone,
            "부서" : dept,
            "연봉" : pay,
            "경력여부" : exp
        }

        added_employee_name = self.employee_dict[employee_code]["이름"]
        print (f"{added_employee_name}님이 추가 되었습니다.")
        print ("당신의 노동을 기대합니다.")
        self.update_json()

    def add(self, num):
        if self.employee_dict["name"] == "이신영":
            self.result += num 
            self.employee_dict["pay"] = self.result
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