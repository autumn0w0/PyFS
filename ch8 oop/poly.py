class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(f"{self.real} + {self.imag}j")

    def __add__(self, num2):
        real_part = self.real + num2.real
        imag_part = self.imag + num2.imag
        return complex(real_part, imag_part)
    
    def __sub__(self, num2):
        real_part = self.real - num2.real
        imag_part = self.imag - num2.imag
        return complex(real_part, imag_part)

num1 = complex(2, 3)
num1.shownumber() # 2 + 3j

num2 = complex(4, 5)
num2.shownumber() # 4 + 5j

num3 = num1 + num2
num3.shownumber() # 6 + 8j

num4 = num1 - num2
num4.shownumber() # -2 + -2j