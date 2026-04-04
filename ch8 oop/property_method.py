class student:
    def __init__(self, chem, math, phy):
        self.chem = chem
        self.math = math
        self.phy = phy
        # self.percentage = str((self.chem + self.math + self.phy) / 3) + "%"
    
    # def cal_percentage(self):
    #     self.percentage = str((self.chem + self.math + self.phy) / 3) + "%"

    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy) / 3) + "%"

student1 = student(80, 90, 85)
print(student1.percentage) # 85.0%

student1.chem = 90
print(student1.percentage) # 90.0% (updated)


