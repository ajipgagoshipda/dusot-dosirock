import csv

items = []  # 재고 데이터를 담을 리스트

class Product:
    count = 0  # 전체 품목 수

    def __init__(self, name, num):
        self.name = name
        self.num = int(num)
        Product.count += 1

    def display_info(self):
        print(f"품목: {self.name}, 수량: {self.num}")

    @classmethod
    def show_count(cls):
        print(f"총 품목 수: {cls.count}")


def load_items(filename):
    """CSV 파일 불러오기"""
    f = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(f)

    header = next(reader)  # 헤더 건너뛰기
    print("📂 CSV 헤더:", header)

    for line in reader:
        name, num = line
        item = Product(name, num)
        items.append(item)

    print("\n=== 초기 재고 목록 ===")
    for i in items:
        i.display_info()
    Product.show_count()

    f.close()



def show_inventory():
    """재고 조회"""
    print("\n=== 📋 현재 재고 현황 ===")
    for i in items:
        i.display_info()
    print("=========================\n")


def add_item():
    """입고"""
    print("\n📦 새 상품 입고")
    name = input("품목 이름: ")
    num = int(input("입고 수량: "))

    # 이미 존재하면 수량만 추가
    for i in items:
        if i.name == name:
            i.num += num
            print(f"✅ {name} 수량이 {num}개 추가되었습니다. (현재 재고: {i.num})")
            return

    # 없으면 새로 추가
    new_item = Product(name, num)
    items.append(new_item)
    print(f"✅ 새 품목 추가: {name} ({num}개)")


def remove_item():
    """출고"""
    print("\n🚚 상품 출고")
    name = input("품목 이름: ")
    num = int(input("출고 수량: "))

    for i in items:
        if i.name == name:
            if i.num >= num:
                i.num -= num
                print(f"🚚 {name} {num}개 출고 완료. (남은 재고: {i.num})")
                if i.num == 0:
                    items.remove(i)
                return
            else:
                print("❌ 재고가 부족합니다.")
                return
    print("❌ 해당 품목이 없습니다.")



def save_items(filename):
    """CSV 파일 저장"""
    f = open(filename, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)
    writer.writerow(["name", "num"])

    for i in items:
        writer.writerow([i.name, i.num])

    print("💾 파일이 업데이트 되었습니다.")
    f.close()

def main():
    filename = "inventory.csv"
    load_items(filename)

    while True:
        cmd = input("\n명령 (입고/출고/재고조회/종료): ").strip()

        if cmd == "입고":
            add_item()
        elif cmd == "출고":
            remove_item()
        elif cmd == "재고조회":
            show_inventory()
        elif cmd == "종료":
            save_items(filename)
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❗ 잘못된 명령입니다. (입고/출고/재고조회/종료 중 하나 선택)")


main()
