
class PipelineFighter:
    def __init__(self, name, hp, power, item, score):
        self.name = name
        self.hp = hp
        self.power = power
        self.item = item
        self.item_score = 0

    def add_item(self, item):
        score = 0
        self.my_item_dict = {
            "빛나는 검" : "강력한 공격력",
            "무적 방패" : "방어력 증가",
            "반짝반짝 요술봉" : "눈부신 공격",
            "마법 포션" : "에너지 부스터"
        }
        print(f"당신이 가진 아이템은 {' | '.join([f'{key}: {value}' for key, value in self.my_item_dict.items()])}입니다.")
        print(f"------"*7)
        my_item = input("사용하실 아이템을 선택해주세요. : ")
        if my_item == "빛나는 검":
            score +=1
        elif my_item == "무적 방패":
            score +=3
        elif my_item == "반짝반짝 요술봉":
            score -=2
        elif my_item == "마법 포션":
            score +=4                        
        if my_item in self.my_item_dict:
            self.item = my_item
            self.item_score = score
            print(f"{my_item}을 선택하였습니다. 아이템의 성능은 {self.item_score}입니다.")
            print(f"三三三三三三"*7)
        else:
            print(f"아이템이 존재하지 않습니다.")

    def attack(self, target):
        """어택 메서드에서는 상대 객체에게 대미지를 준다."""
        damage = self.power + self.item_score

        # 대미지를 주면 상대 객체의 hp가 줄어든다?
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        
        print (f"{self.name}의 공격으로 {target.name}의 hp가 {target.hp} 남았습니다.")

    def is_alive(self):
        alive = self.hp > 0 # bool
        return alive


seonil = PipelineFighter("선일", 15, 5, "-", 0)
junsoo = PipelineFighter("준수", 10, 7, "-", 0)
seonil.add_item("-")
junsoo.add_item("-")

while seonil.is_alive() and junsoo.is_alive():

    print (f"👊 {seonil.name}님의 {seonil.item}을 사용한 공격이 시작됩니다 👊")
    seonil.attack(junsoo) # 테스트 해본다.
    if not junsoo.is_alive():
        print("༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽엉엉흐엉어허어엉ㅇ어ㅠㅓ허허허휴ㅠㅠㅠㅠㅎ어어유ㅠㅠㅠㅠ파하규ㅠㅠㅠ༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽")
        print (f"{junsoo.name}가 쓰러졌다. 피비린내 나는 싸움이었다.")
        break

    print (f"🥊 {junsoo.name} 님의 {junsoo.item}을 사용한 공격이 시작됩니다 🥊")
    junsoo.attack(seonil) # 테스트 해본다.
    if not seonil.is_alive():
        print("༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽༼ ˃ɷ˂ഃ༽엉엉흐엉어허어엉ㅇ어ㅠㅓ허허허휴ㅠㅠㅠㅠㅎ어어유ㅠㅠㅠㅠ파하규ㅠㅠㅠ༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽༼;´༎ຶ ۝ ༎ຶ༽")
        print (f"{seonil.name}이가 쓰러졌다. 정의는 승리하지 못했다.")
        break