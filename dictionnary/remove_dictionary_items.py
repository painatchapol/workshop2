thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# {'brand': 'Ford', 'year': 1964}


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()  # ตัวสุดท้าย
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# {'brand': 'Ford', 'year': 1964}

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# {}