items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 16)
]

# def sort_items(item):
#    return item[1]

# items.sort(key=sort_items)
# print(items)

# Code with Lambda
items.sort(key=lambda item: item[1])
print(items)
