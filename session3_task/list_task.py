      
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def introduce(self):
        print(f"이름 {self.name} 나이 {self.age} 키{self.height}")
        
    def yell(self):
        print("아?")
    
class Developer(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    keyboard = "기계식"
        
    def yell(self):
        print("어?")
        
class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease
        
class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        
    def yell(self):
        print("개발자님 여기 오류있어요")
        
    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야 하나...")
        Developer.keyboard = "멤브레인"
        
d1 = Developer("이주홍", 25, 186 )
d2 = Designer("지석진", 28, 170, '두통')
p1 = ProductManager("윤소희", 30, 180)
d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()

