base = {
    "item 1": 45.50,
    "item 2":35,
    "item 3": 41.30,
    "item 4":55,
    "item 5 ": 24}

for i in range(3):
    max_value = 20
    max_value_key = ""
    for key, value in base.items():
        if value > max_value:
            max_value = value
            max_value_key = key
    print(max_value_key, base[max_value_key])
    del base[max_value_key]
