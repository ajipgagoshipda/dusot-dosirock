import csv
items = []

class product:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        
    
    def display_info(self):
        print(f"품목: {self.name}, 갯수: {self.num}")

    
def load_items(filename):
    f = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)
    
    for line in reader:
        name, num = line
        item = product(name, int(num))
        items.append(item)

    print("__ 재고 목록 __")
    for i in items:
        i.display_info()
    
    f.close()

def show_inventory():
    print("\n __ 현재 재고 현황 __")
    for i in items:
        i.display_info()
    print("_____________________\n")

def add_item():
    print("\n 새 상품 입고")
    name = input("품목 이름: ")
    num = int(input("입고 수량: "))

    for i in items:
        if i.name == name:
            i.num += num
            print(f"{name} 수량이 {num}개 추가되었습니다. (현재 재고: {i.num})")
            return
        
    new_item = product(name, num)
    items.append(new_item)
    print(f" 새 품목 추가: {name} {num}개")

def remove_item():
    print("\n 상품출고")
    name = input("품목 이름: ")
    num = int(input("출고 수량: "))
    
    for i in items:
        if i.name == name:
            if i.num >= num:
                i.num -= num
                print(f"{name} {num}개 출고 완료. (남은 수량: {i.num}))")
                if i.num == 0:
                    items.remove(i)
                return
            else:
                print("재고가 부족합니다.")
                return
            
    print("해당 품목이 없습니다.")

def save_items(filename):
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)
    writer.writerow(["name", "num"])

    for i in items:
        writer.writerow([i.name, i.num])

    print("파일이 업데이트 되었습니다.")
    f.close()

def main():
    filename = "inventory.csv"
    load_items(filename)

    while True:
        cmd = input("\n뭐할꺼임? (입고 / 출고 / 재고조회 / 종료): ")

        if cmd == "입고":
            add_item()
        elif cmd == "출고":
            remove_item()   
        elif cmd == "재고조회":
            show_inventory()        
        elif cmd == "종료":
            save_items(filename)
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 명령입니다. (입고 / 출고 / 재고조회 / 종료)중에서 선택")


main()



