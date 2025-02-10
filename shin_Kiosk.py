menu_list = {
    "김밥" : 4500,
    "오일파스타" : 8000,
    "햄버거" : 4000,
    "감자튀김" : 3000,
    "치킨너켓" : 3000,
    "콜라" : 1500,
    "사이다" : 1500    
}

order_menulist = {}

def menu_check():
    for key, value in menu_list.items():
        print(f"메뉴 | {key} 가격 : {value}")

def add_order():
    order_menu = input("메뉴를 선택해주세요. : ")
    if order_menu not in menu_list:
        print("입력하신 메뉴는 판매하지 않습니다.")
        return
    quantity = int(input(f"{order_menu}의 수량을 입력해주세요. :"))

    if order_menu in order_menulist:
        order_menulist[order_menu] += quantity
    else:
        order_menulist[order_menu] = quantity

    print(f"{order_menu} {quantity}개가 주문목록에 추가되었습니다.")
    print(f"장바구니 속 메뉴: {order_menulist}")

def delete_order():
    print(f"당신의 장바구니 속에는 {order_menulist}가 있습니다.")
    del_menu = input("삭제할 메뉴를 입력해주세요. : ")
    if del_menu not in order_menulist:
        print("입력하신 메뉴는 장바구니에 없습니다.")

    if del_menu in order_menulist:
        del order_menulist[del_menu]
        print(f"메뉴가 삭제되었습니다. 장바구니에는 {order_menulist}가 담겨있습니다.")

def order():
    if not order_menulist:
        print("장바구니가 비어있습니다. 메뉴를 추가해주세요.")
    total_price = 0
    for order_menu, quantity in order_menulist.items():
        price = menu_list[order_menu] * quantity
        print (f"{order_menu}는 {quantity}개, 가격은 {price} 입니다.")
        total_price += price
    print(f"총 가격은 {total_price}입니다.")

while True:
    command = input("주문을 하시겠습니까? (메뉴 확인, 추가, 삭제, 주문) : ")
    if command == "메뉴 확인":
        menu_check()
        
    elif command == "추가":
        add_order()

    elif command == "삭제":
        delete_order()

    elif command == "주문":
        order()