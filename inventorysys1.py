import csv
import os

class Inventory:
    def __init__(self, filename="inventory.csv"):
        self.filename = filename
        self.items = {}
        self.load_from_csv()

    def load_from_csv(self):
        """CSV 파일에서 데이터 불러오기"""
        if not os.path.exists(self.filename):
            print(" CSV 파일이 없습니다.")
            return
        with open(self.filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                num = int(row["num"])
                self.items[name] = num

    def save_to_csv(self):
        """CSV 파일로 저장"""
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "num"])
            for name, num in self.items.items():
                writer.writerow([name, num])

    def add_item(self, name, count):
        """입고 처리"""
        self.items[name] = self.items.get(name, 0) + count
        self.save_to_csv()
        print(f" {name} {count}개 입고 완료 (현재 재고: {self.items[name]})")

    def remove_item(self, name, count):
        """출고 처리"""
        if name not in self.items:
            print(" 해당 품목이 존재하지 않습니다.")
            return
        if self.items[name] < count:
            print(f" 재고 부족 ({name} 재고: {self.items[name]}개)")
            return
        self.items[name] -= count
        if self.items[name] == 0:
            del self.items[name]
        self.save_to_csv()
        print(f" {name} {count}개 출고 완료")

    def show_inventory(self):
        """현재 재고 현황 출력"""
        if not self.items:
            print(" 재고가 비어 있습니다.")
            return
        print("\n===  현재 재고 현황 ===")
        for name, num in self.items.items():
            print(f"{name}: {num}개")
        print("=========================\n")


class InventoryApp:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            command = input("명령을 입력하세요 (입고/출고/재고조회/종료): ").strip()
            if command == "입고":
                name = input("품목 이름: ").strip()
                try:
                    count = int(input("입고 수량: "))
                    self.inventory.add_item(name, count)
                except ValueError:
                    print("]] 숫자를 입력하세요.")
            elif command == "출고":
                name = input("품목 이름: ").strip()
                try:
                    count = int(input("출고 수량: "))
                    self.inventory.remove_item(name, count)
                except ValueError:
                    print(" 숫자를 입력하세요.")
            elif command == "재고조회":
                self.inventory.show_inventory()
            elif command == "종료":
                print(" 프로그램을 종료합니다.")
                break
            else:
                print(" 잘못된 명령입니다. (입고/출고/재고조회/종료 중 하나 입력)")
                

if __name__ == "__main__":
    app = InventoryApp()
    app.run()
