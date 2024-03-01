dictOne = {"a": 1, "b": 2, "c": 3}
dictTwo = {"b": 4, "c": 5, "d": 6}

common_keys = set(dictOne.keys()) & set(dictTwo.keys())

print(common_keys)