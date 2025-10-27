class Dog:
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    def bark(self):
        print(f"{self.name}가 멍멍!하고 짖습니다.")

    @classmethod
    def show_count(cls):
        print(f"현재 강아지수 {cls.count}")

    @staticmethod
    def sound():
        print("개는 멍멍 소리를 냅니다.")

dog1 = Dog("몽글이")
dog2 = Dog("깽이")

dog1.bark()
dog2.bark()
Dog.show_count()
Dog.sound()