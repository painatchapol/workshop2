# EX2
dict1 = {"name": "Natchapol", "age": "22"}
dict2 = {"name": "Natchapol", "age": "22"}
dict3 = dict1

print(dict1 is dict3)  # True
print(dict1 is dict2)  # False
print(dict1 is not dict2)  # d1ไม่ใช่d2 True
print(dict1 == dict2)  # True