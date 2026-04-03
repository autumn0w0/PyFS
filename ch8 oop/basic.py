# class Student:
#     name = "autumn"

# s1 = Student()
# print(s1.name)  # autumn 

# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# s1 = Student("autumn")
# print(s1.name)  # autumn

#del keyword
class Student:
    def __init__(self, fullname):
        self.name = fullname

s1 = Student("autumn")
print(s1.name)
del s1
# print(s1.name)  # NameError: name 's1' is not defined