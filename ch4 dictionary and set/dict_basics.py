info = {"name": "Autumn", 
        "age": 30, 
        "city": "New York",
        "hobbies": ["reading", "traveling", "cooking"],
        "is_student": False}
print(info)
print(info["name"])

# null dict
null_dict = {}
print(null_dict)

#nested dict
student = {"name": "Alice",
           "marks": {"math": 85, "science": 90, "literature": 78},
           "passed": True}
print(student)
print(student["marks"]["science"])