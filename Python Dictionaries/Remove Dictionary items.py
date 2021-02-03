# EX1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

# EX2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)

# EX3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict.pop["model"]
print(thisdict)

# EX4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
