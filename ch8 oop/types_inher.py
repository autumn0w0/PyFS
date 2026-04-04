#single and multiple inheritance
class car:
    @staticmethod
    def start():
        print("car is starting")

    @staticmethod
    def stop():
        print("car is stopping")    

class bmw(car):
    def __init__(self, model):
        self.model = model

class bmw_x5(bmw):
    def __init__(self, type, year, model):
        super().__init__(model)
        self.type = type
        self.year = year

car1 = bmw_x5("petrol", 2020, "X5")

print(car1.type)
print(car1.year)
print(car1.model)
car1.start()

#multi level inheritance
class A:
    vara = "welcome to class A"

class B:
    varb = "welcome to class B"

class C(A, B):
    varc = "welcome to class C"

c1 = C()
print(c1.vara) # welcome to class A
print(c1.varb) # welcome to class B
print(c1.varc) # welcome to class C

#super method
class car:
    @staticmethod
    def start():
        print("car is starting")
    
    @staticmethod
    def stop():
        print("car is stopping")

    def __init__(self, type):
        self.type = type

class bmw(car):
    def __init__(self, model, type):
        super().__init__(type)
        self.model = model

car1 = bmw("X5", "petrol")
print(car1.model) # X5
print(car1.type) # petrol