# EX1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output : {'brand': 'Ford', 'year': 1964}

# EX2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output : {'brand': 'Ford', 'model': 'Mustang'}

# EX3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output : {'brand': 'Ford', 'year': 1964}

# EX4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# Output : {}
