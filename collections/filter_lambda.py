items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 16)
]

prices_filter = list(filter(lambda item: item[1] >= 10, items))
print(prices_filter)

# COMPREHENSIONS
price_filter = [item for item in items if item[1] >= 10]
print(price_filter)
